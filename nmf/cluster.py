#from nmfplus import *
import random
import numpy as np
import scipy.sparse as sp


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

    f.close()

    print n_movies,n_users

    return((sp.csr_matrix((values,(row,column)),shape=(n_movies,n_users)),
            movie_ids,user_ids,n_movies,n_users))

#    (B,movie_seeds) = make_sparse_rand_vectors(n_clusters,dim)
def make_sparse_rand_vectors(n_clusters,m,dim):
    B = np.zeros((m,dim))

    movie_seeds = []
    
    for i in xrange(n_clusters):
        row = random.randint(0,m-1)
        movie_seeds.append(row)
        for j in xrange(dim):
            B[row,j] = -1.0 + 2.0*random.randint(0,1)

    print("movie_seeds", movie_seeds)
        
    return (B,movie_seeds)

def predict_with_cluster(user,movie,At,graph):
    if ((user >= At.shape[0]) or (movie >= At.shape[1])):
        return(0.0,0.0)
    
    (n_movies,n_users) = At.shape
    
    movie_neighbors = graph.getrow(movie).transpose()
    #print movie_neighbors
    val = 0
    #print At.shape
    #print user,movie
    for row_col_index in xrange(At.indptr[user],At.indptr[user+1]):
        rated_movie = At.data[row_col_index]
        rated_movie_neighbors = graph.getrow(rated_movie)
        #print rated_movie_neighbors
        score = rated_movie_neighbors.dot(movie_neighbors)[0,0]
        print "score", score
        print rated_movie,movie
        print rated_movie_neighbors
        print movie_neighbors

        val += score
        #print "val", val
        
    return (val,At.indptr[user+1]-At.indptr[user])

def inverse_map(the_mapping):
    reverse_mapping = {}
    for key in the_mapping.keys():
        reverse_mapping[the_mapping[key]] = key
    return reverse_mapping



def spnorm(a):
    return np.sqrt(((a.data**2).sum()))

def cluster_prediction(filename,test_filename,dir_prefix="./cluster"):
    outfile = open(dir_prefix+"test.predictions","w")

    (A,movie_ids,user_ids,m_count,u_count) = read_data(filename)

    reverse_user = inverse_map(user_ids)
    reverse_movie = inverse_map(movie_ids)
    At = A.transpose()
    n_samples = 4000
    
    n_clusters = 200
    n_rounds = 3
    graph = sp.lil_matrix((m_count,m_count))
    degree = 2
    dim = 30
    iterations = 1
    counts = [0 for x in xrange(n_clusters)]


    for rnd in xrange(n_rounds):
        (B,movie_seeds) = make_sparse_rand_vectors(n_clusters,m_count,dim)

        seed_indices = {}
        for i in xrange(len(movie_seeds)):
            seed_indices[movie_seeds[i]] = i

        H = B
        for i in xrange(iterations):
            H = A.dot(At.dot(H))

        for c in xrange(m_count):
            best_so_far = []
            for m in movie_seeds:
                v = B[m,]
                val = np.dot(H[c,],B[m,])
                if len(best_so_far) < degree:
                    #if (val > np.dot(B[m,],B[m,])):
                    if (val > 0):
                        best_so_far.append((val,m))
                else:
                    m_now = m
                    for i in xrange(degree):
                        if val > best_so_far[i][0]:
                            t_val = val
                            t_m_now = m_now
                            (val,m_now) = best_so_far[i]
                            best_so_far[i] = (t_val,t_m_now)

            #print ("movie, vals", c,best_so_far)

            for (val,m) in best_so_far:
                # print ("c,m,val", c,m, val)
                graph[c,m] =  1.0 # val
                counts[seed_indices[m]]+=1

        print "counts",counts

    n_smaples = 10000
    graph = graph.tocsr()
    print "graph", graph.shape,graph.nnz,spnorm(graph)

    trainA = A
    train_m_count = m_count
    train_u_count = u_count
    At = At.tocsr()


    (A,movie_ids,user_ids,m_count,u_count) = read_data(test_filename,movie_ids,user_ids,m_count,u_count,discard=True)
    
    #outfile2 = open(dir_prefix+"test.predictions2","w")

    print ("Total of %d test ratings" % A.nnz)
    (n,m) = A.shape
    cnt=0

    # print_int = min(A.nnz/10,1000)
    # for row in xrange(n):
    #     for row_col_index in xrange(A.indptr[row],A.indptr[row+1]):
    #         col = A.indices[row_col_index]
    #         elt = A.data[row_col_index]
    #         (val1,val2) = predict_with_cluster(col,row,At,graph)
    #         cnt+=1
    #         if (cnt%print_int== 0):
    #             print "cnt,movie,user,val1", cnt, row,col,val1
    #         print >> outfile, "%s,%s,%0.5f" % (reverse_movie[row],reverse_user[col], val1)

    print_int = 100
    for row in xrange(min(n_samples,A.nnz)):
        i = random.randint(0,A.nnz -1)
        row = find_index(A.indptr,i)            
        col = A.indices[i]
        (val1,deg) = predict_with_cluster(col,row,At,graph)
        cnt+=1
        if (cnt%print_int == 0):
            print "cnt,movie,user,deg,val1", cnt, row,col,deg,val1
        print >> outfile, "%s,%s,%0.5f,%0.5f" % (reverse_movie[row],reverse_user[col], val1,deg)
        

    # Test on completely random pairs
    print ("Doing random pairs")
    print_int = 100
    outfile = open(dir_prefix + "test.rndpairs.predictions","w")
    for n_pairs in xrange(n_samples):
        row = random.randint(0,n-1)
        col = random.randint(0,m-1)
        (val1,deg) = predict_with_cluster(col,row,At,graph)
        cnt+=1
        if (cnt%print_int == 0):
            print "cnt,movie,user,deg,val1", cnt, row,col,deg,val1
        print >> outfile, "%s,%s,%0.5f,%0.5f" % (reverse_movie[row],reverse_user[col], val1,deg)


    # Test on difficult distribution that ephasizes non-rated pairs where movies and users
    # are chosen based on rating count.
    print ("Doing random difficult pairs")
    outfile = open(dir_prefix+"test.hard.rndpairs.predictions","w")
    for n_pairs in xrange(n_samples):
        i = random.randint(0,A.nnz -1)
        row = find_index(A.indptr,i)
        j = random.randint(0,A.nnz -1)
        col = A.indices[j]
        if (row > A.shape[0]-1):
            print row, A.shape, "what is going on"
            continue
        if (col > A.shape[1]-1):
            print col, A.shape, "what is going on"
            continue
        (val1,deg) = predict_with_cluster(col,row,At,graph)

        if (A[row,col] > 0 or trainA[row,col] > 0):
            continue
        cnt+=1
        if (cnt%print_int == 0):
            print "cnt,movie,user,deg,val1", cnt, row,col,deg,val1
        print >> outfile, "%s,%s,%0.5f,%0.5f" % (reverse_movie[row],reverse_user[col], val1,deg)

