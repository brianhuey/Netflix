import numpy as nd
import scipy.sparse as sp
import random as r
import math

def mult(B,X):
    pass

def spread(X):
    pass

scale = 2
start = .1
p = .07


# Make all negative values positive.
# by simply rounding up.
def fix_barrier(X,p):
    (n,k) = X.shape

    level = math.sqrt(p)
    negatives = 0
    for i in xrange(0,n):
        for j in xrange(0,k):
            if X[i,j] < 0:
                X[i,j] = level*start
                negatives += 1
            if X[i,j] < level:
                X[i,j] = X[i,j]*scale
    print ("negatives fixed:", negatives)
    return (X)

coverage = 2 # should be more than 1.

# Samples rows of the matrix and averages
# them to produce a k row "approximation"
# of the original matrix.
def init_vecs(A,k,left=True):
    B = A
    if left == True:
        B = A.transpose()
    result = []
    for i in xrange(0,k):
        v = []
        for j in xrange(0,B.shape[1]):
            if r.randint(0,k) < coverage:
                v.append(1.0)
            else:
                v.append(0.0)

        result.append(B.dot(v)*(1.0/(coverage*k)))
    return nd.array(result)


# Reading the data from the netflix files into matrix
#  - returns the dictionaries for translating between row/col to movie/user
#  - will take dictionary so that one can translate test data to use
#  - same matrix that was formed using training data.
def read_data(filename,movie_ids={},user_ids={},n_movies=0,n_users=0,discard =False):

    f = open(filename)

    row = []
    column = []
    values = []

    for line in f:
        fields = line.strip().split(",")

        movie_id = fields[0]
        user_id = fields[1]

        if discard and ((not movie_id in movie_ids) or (not user_id in user_ids)):
            continue

        if not movie_id in movie_ids:
            movie_ids[movie_id] = n_movies
            n_movies+=1
        if not user_id in user_ids:
            user_ids[user_id] = n_users
            n_users += 1

        row.append(movie_ids[movie_id])
        column.append(user_ids[user_id])
        # values.append(float(fields[2]))
        values.append(1.0)

    return((sp.csr_matrix((values,(row,column)),shape=(n_movies,n_users)),
            movie_ids,user_ids,n_movies,n_users))

min_scale = .1

#  This code does gram-schmidt orthogonalization,
#  except it makes sure all entries are positive.
def normalize_kind_of(X,p):
    (k,n) = X.shape
    #return (X)

    # won't normalize so much.
    level = math.sqrt(p)
    total_normalization = 0.0
    total_old_norm = 0.0
    total_new_norm = 0.0

    for i in xrange(0,k):
        a = X[i,:]
        old_norm = math.sqrt(nd.dot(a,a))
        total_old_norm += old_norm

        # Make ith factor "orthogonal" to all previous factors.
        for j in xrange(1,i):
            a = X[i,:]
            b = X[j,:]
            mag_b_squared = nd.dot(b,b)
            mag_b = math.sqrt(mag_b_squared)
            value = nd.dot(a,b)
            mag_a = math.sqrt(nd.dot(a,a))

            # Main stuff here.
            X[i,:] = a - (value/mag_b)*(b/mag_b)

            # Error checking code below.
            normalization_factor = abs(value)/(mag_a*mag_b)
            new_mag = math.sqrt(nd.dot(a,a))
            if (new_mag > mag_a +.1):
                print("ugh",new_mag,mag_a,value)
                print ("mag b", mag_b, math.sqrt(nd.dot(b/mag_b,b/mag_b)))
            if normalization_factor > 1.01:
                print("sqrt a*a", math.sqrt(nd.dot(a,a)))
                print("a*b", nd.dot(a,b))
                print ("sqrt b*b", math.sqrt(nd.dot(b,b)))
                print normalization_factor
                print a
                print b
            total_normalization += normalization_factor

            # Make sure all entries are positive.
            for l in xrange(0,k):
                X[i,l] = max(X[i,l],min_scale*level)

        # Track how much orthogonalization wer are doing
        # in case we are curious
        new_norm = math.sqrt(nd.dot(X[i,:],X[i,:]))
        total_new_norm += new_norm

    # print ("total normalization", total_normalization)
    # print("total new norm", total_new_norm)
    # print ("total old norm", total_old_norm)

    return X



def evaluate_gradients(A,U,V,p,p_sample_size):
    (n,m) = A.shape
    mse = 0.0
    count = 0
    del_U = nd.zeros(U.shape)
    del_V = nd.zeros(V.shape)
    index_hash = {}
    for row in xrange(n):
        for row_col_index in xrange(A.indptr[row],A.indptr[row+1]):
            col = A.indices[row_col_index]
            elt = A.data[row_col_index]
            index_hash[(row,col)] = True

            diff = elt - nd.dot(U[row,:],V[:,col])

            # the derivation of (elt - U*V)^2 is -2V (elt- U*V) with respect to U
            del_U[row,:] -= V[:,col]*diff*(1.0*n/A.nnz)

            # and vice versa.
            del_V[:,col] -= U[row,:]*diff*(1.0*m/A.nnz)

            # Compute Function.
            mse += diff*diff

            count+=1

    # Make random unrated pairs have 0's to make sure
    # we don't stupidly output all
    # ones matrix.
    for i in xrange(p_sample_size):
        row = r.randint(0,n-1)
        col = r.randint(0,m-1)
        if (row,col) in index_hash:
            continue

        diff = p - nd.dot(U[row,:],V[:,col])

        del_U[row,:] -= V[:,col]*diff*(n*1.0/p_sample_size)
        del_V[:,col] -= U[row,:]*diff*(m*1.0/p_sample_size)

        mse += diff*diff
        count+=1

    return (mse/(1.0*count),del_U,del_V)

iterations = 1
step_size = .05

# Main Procedure: iteratively run gradient descent
#  method.
def hack_nmf_iter(A,k,p,p_sample_size):
    (n,m) = A.shape
    U = nd.transpose(init_vecs(A,k,left=False))
    V = init_vecs(nd.transpose(A),k,left= False)

    print("nnz ", A.nnz)
    print("shape U", U.shape)
    print("shape V", V.shape)
    p_sample_size  = A.nnz

    AT = A.transpose()

    for i in xrange(0,iterations):

        #Compute Gradients (and function.)
        (error,del_U,del_V) =  evaluate_gradients(A,U,V,p,p_sample_size)
        print("rmse", math.sqrt(error), i)

        # do Step for U
        U -= step_size*del_U
        U = fix_barrier(U,p)
        U = nd.transpose(normalize_kind_of(nd.transpose(U),p))

        #Do step for V
        V -= step_size*del_V
        V = normalize_kind_of(V,p)
        V = nd.transpose(fix_barrier(nd.transpose(V),p))

        # print("row 8 of U", U[8,:5])
        # print("row 9 of U", U[9,:5])

        # print("column 8 of V", V[:5,8])
        # print("column 9 of V", V[:5,9])

    return(U,V)


#### Testing below here....

#Generating random continuous matrix with
# some large and many small entries.
def gen_rand_factor(n,k,p):

    level = math.sqrt(p)
    U = nd.zeros((n,k))
    ones = []
    for i in xrange(0,n):
        for j in xrange(0,k):
            if (r.randint(0,int(1.0/level)) < 1):
                U[i,j] = 1.0
            else:
                scale = r.randint(-1,1)
                U[i,j] = level*(2**scale)
    return (U)

# Generate a random 0-1 matrix
#  which is sparse.
def gen_rand_factor(n,k,p,binary=True):

    level = math.sqrt(p)
    U = nd.zeros((n,k))
    ones = []
    for i in xrange(0,n):
        for j in xrange(0,k):
            if (r.randint(0,int(1.0/level)) < 1):
                U[i,j] = 1.0
            else:
                if (not binary):
                    scale = r.randint(-1,1)
                    U[i,j] = level*(2**scale)
    return (U)

# Testing with random matrix.
def test_nmf_iter(n,m,k,p,binary=False):
    U = fix_barrier(gen_rand_factor(n,k,p,binary),p)
    V = nd.transpose(fix_barrier(gen_rand_factor(m,k,p,binary),p))

    A = nd.dot(U,V)
    A = sp.csr_matrix(A,(n,n))
    (error,del_U,del_V) =  evaluate_gradients(A,U,V,p,100)

    print("original evaluate score", error)

    hack_nmf_iter(A,k,p,100)

# Testing with factor model
# where there are k factors
# and movies are in a random dn of them
# and users are in a random dm of them.
# If dn = dm =1, each user likes only
# one type of movie. Each movie is only
# of one type.
def k_types_test_nmf(n,m,k,dn,dm):
    U = nd.zeros((n,k))
    V = nd.zeros((k,m))

    for i in xrange(0,n):
        for cnt  in xrange(0,dn):
            factor = r.randint(0,k-1)
            U[i,factor] = 1

    for i in xrange(0,m):
        for cnt  in xrange(0,dm):
            factor = r.randint(0,k-1)
            V[factor,i] = 1

    A = sp.csr_matrix(nd.dot(U,V),(n,m))

    (error,del_U,del_V) =  evaluate_gradients(A,U,V,0,A.nnz)

    print("original evaluate score", error)
    p = .07
    (U1,V1) = hack_nmf_iter(A,2*k,p,100)


# Driver loop.
def driver_movie_data(filename,k):
    A = read_data(filename)

    (U1,V1) = hack_nmf_iter(A,2*k,p,100)


# Used to compute movie to row, user to col translation.
def inverse_map(the_mapping):
    reverse_mapping = {}
    for key in the_mapping.keys():
        reverse_mapping[the_mapping[key]] = key
    return reverse_mapping

# Print the highest valued movies in a movie
# factor.
def print_movie_factor(U,reverse_movie,i,to_print=20):

    (n,k) = U.shape

    f = open("../data/movie_titles.txt")

    movie_id_to_title = {}

    for line in f:
        fields = line.strip().split(",")

        movie_id_to_title[fields[0]] = fields[2]

    pairs = []
    for j in xrange(n):
        pairs.append((reverse_movie[j],U[j][i]))

    s_pairs = sorted(pairs, key= lambda pair: pair[1],reverse=True)

    for k in xrange(to_print):
        print ("%s, %0.2f" % (movie_id_to_title[s_pairs[k][0]], s_pairs[k][1]))


# Helper function for finding ith nonzero entry
# in sparse matrix representation
def find_index(array,val,left=0, right = False):
    if not right:
        right = len(array)
    if right-left <= 1:
        return left
    else:
        mid = (right+left)/2
        if (val >= array[mid]):
            return find_index(array,val,left=mid,right=right)
        else:
            return find_index(array,val,left=left,right=mid)


# Main Evaulation loop.
def driver_movie_data_test(train_filename,test_filename,k):

    (A,movie_ids,user_ids,m_count,u_count) = read_data(train_filename)

    # Do nnmf
    (U1,V1) = hack_nmf_iter(A,k,.07,16*A.nnz)

    # Read test data
    (A,movie_ids,user_ids,m_count,u_count) = read_data(test_filename,movie_ids,user_ids,m_count,u_count,discard=True)
    (error,del_U,del_V) =  evaluate_gradients(A,U1,V1,.07,16*A.nnz)

    reverse_user = inverse_map(user_ids)
    reverse_movie = inverse_map(movie_ids)


    # Test on Ratings!
    outfile = open("test.predictions","w")
    print ("Doing %d test ratings" % A.nnz)
    (n,m) = A.shape
    for row in xrange(n):
        for row_col_index in xrange(A.indptr[row],A.indptr[row+1]):
            col = A.indices[row_col_index]
            elt = A.data[row_col_index]
            print >> outfile, "%s,%s,%0.2f" % (reverse_movie[row],reverse_user[col], nd.dot(U1[row,:],V1[:,col]))

    # Test on completely random pairs
    outfile = open("test.rndpairs.predictions","w")
    for n_pairs in xrange(1000):
        row = r.randint(0,n-1)
        col = r.randint(0,m)
        print >> outfile, "%s,%s,%0.2f" % (reverse_movie[row],reverse_user[col], nd.dot(U1[row,:],V1[:,col]))

    # Test on difficult distribution that ephasizes non-rated pairs where movies and users
    # are chosen based on rating count.
    outfile = open("test.hard.rndpairs.predictions","w")
    for n_pairs in xrange(1000):
        i = r.randint(0,A.nnz -1)
        row = find_index(A.indptr,i)
        j = r.randint(0,A.nnz -1)
        col = A.indices[j]
        if (row > A.shape[0]-1):
            print row, A.shape, "what is going on"
            continue
        if (col > A.shape[1]-1):
            print col, A.shape, "what is going on"
            continue
        #print "shape,row,col", A.shape,row,col
        # if (A[row][col] > 0):
        #     continue
        print >> outfile, "%s,%s,%0.2f" % (reverse_movie[row],reverse_user[col], nd.dot(U1[row,:],V1[:,col]))


    print ("test rsme", math.sqrt(error))
    for i in xrange(k):
        print ("Factor:", i)
        print_movie_factor(U1,reverse_movie, i)
    return(U1,V1,reverse_movie,reverse_user)


# Baseline movie prediction based on user/movie counts and independence.
def user_movie_pred(test_file_name, outfile_name = 'baseline.out'):
    user_file = open("../baseline/user_total/user_total_fromAWS")
    movie_file = open("../baseline/movie_total/movie_total_fromAWS")
    test_file = open(test_file_name)

    total_movies = 17750 # Calculated
    total_users = 480189 # Calculated
    overall_rate = (100480507/float(total_movies * total_users))
    movie_tots = {}
    ratings_by_user = {}


    for line in test_file:
        fields = line.strip().split(",")
        if not fields[1] in ratings_by_user:
            ratings_by_user[fields[1]] = {}
        ratings_by_user[fields[1]][fields[0]] = 0
    test_file.close()

    for line in movie_file:
        fields = line.strip().split()
        if fields[0] == 'total':
            continue
        movie_tots[fields[0]] = float(fields[1])

    for line in user_file:
        fields = line.strip().split()
        if fields[0] == 'total':
            continue
        user_id = fields[0]
        user_count = float(fields[1])
        if user_id in ratings_by_user:
            for movie in ratings_by_user[user_id]:
                movie_count = movie_tots[movie]
                ratings_by_user[user_id][movie] = movie_count*user_count/(total_users*total_movies)

    outfile = open(outfile_name,"w")

    test_file = open(test_file_name)
    for line in test_file:
        fields = line.strip().split(",")
        user_id = fields[1]
        movie_id = fields[0]
        print >> outfile, "%s,%s, %0.5f" % (movie_id,user_id,ratings_by_user[user_id][movie_id])

#test_nmf_iter(100,100,10,.7,binary=True)

#test_nmf_iter(100,100,10,.7)

#k_types_test_nmf(100,100,10,1,1)

#driver_movie_data("../data_sample/data_set_sample.txt",10)
#driver_movie_data("../data/sample.100K.txt",5)

(U,V,reverse_movie,reverse_user) = driver_movie_data_test("../data/sample.100K.train.txt",
                                                          "../data/sample.100K.test.txt",5)

# Doing baseline tests on ratings.
user_movie_pred("test.predictions",
                outfile_name = 'baseline.ratings.predictions')

# Doing baseline tests on random pairs.
user_movie_pred("test.rndpairs.predictions",
                outfile_name = "baseline.rndpairs.predictions")

# Doing baseline tests on random pairs from sample from movie/user pairs weighted independently by count.
user_movie_pred("test.hard.rndpairs.predictions",
                outfile_name = "baseline.hard.rndpairs.predictions")
