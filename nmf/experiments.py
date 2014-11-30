from nmfplus import *
from bayes import *
import math
import random
import glob

def read_more_data(filename,row=[],col=[],values=[],movie_ids={},user_ids={},n_movies=0,n_users=0,discard =False):

    print " opening ", filename

    f = open(filename)

    for line in f:
        fields = line.strip().split(",")

        movie_id = fields[0]
        user_id = fields[1]

        if discard and ((not movie_id in movie_ids) or (not user_id in user_ids)):
            continue

        #print "adding movie, user", movie_id,user_id

        if not movie_id in movie_ids:
            movie_ids[movie_id] = n_movies
            n_movies+=1
        if not user_id in user_ids:
            user_ids[user_id] = n_users
            n_users += 1

        row.append(movie_ids[movie_id])
        col.append(user_ids[user_id])
        # values.append(float(fields[2]))
        values.append(1.0)

    return (row,col,values,movie_ids,user_ids,n_movies,n_users)


def read_data_from_files(files,movie_ids={},user_ids={},n_movies=0,n_users=0,discard =False):

    row = []
    col = []
    values = []
    for f_name in files:
        (row,col, values,movie_ids,user_ids,n_movies,n_users) = read_more_data(f_name,row,col,values,movie_ids,user_ids,n_movies,n_users,discard)

    A = sp.csr_matrix((values,(row,col)),shape=(n_movies,n_users))

    print "Making matrix with ", len(row), " non zeros with shape ", n_movies, n_users

    return(A,movie_ids,user_ids,n_movies,n_users)


def driver_movie_data_validate_bayes(train_files = [],validation_files = [],test_files =[],add_zeros =True,k=10,hard=False):

    print train_files

    (A,movie_ids,user_ids,m_count,u_count) = read_data_from_files(train_files)

    # Do nnmf
    (U1,V1) = hack_nmf_iter(A,k,.07,16*A.nnz,hard)

    # Read validation data
    (A,movie_ids,user_ids,m_count,u_count) = read_data_from_files(validation_files,movie_ids,user_ids,m_count,u_count,discard=True)

    (error,del_U,del_V) =  evaluate_gradients(A,U1,V1,.07,16*A.nnz,hard)
    print ("validation rsme", math.sqrt(error))

    reverse_user = inverse_map(user_ids)
    reverse_movie = inverse_map(movie_ids)

    # Test on Ratings!
    validation_filename = "validation.predictions"
    outfile = open(validation_filename,"w")
    valid_hash = {}
    print ("Doing %d validation ratings" % A.nnz)
    (n,m) = A.shape
    for row in xrange(n):
        for row_col_index in xrange(A.indptr[row],A.indptr[row+1]):
            col = A.indices[row_col_index]
            valid_hash[(row,col)] = True
            elt = A.data[row_col_index]
            print >> outfile, "%s,%s,%0.2f" % (reverse_movie[row],reverse_user[col], nd.dot(U1[row,:],V1[:,col]))

    outfile.close()

    # Test on completely random pairs

    outfile = open("validation.rndpairs.predictions","w")
    for n_pairs in xrange(1000):
        row = r.randint(0,n-1)
        col = r.randint(0,m-1)
        print >> outfile, "%s,%s,%0.2f" % (reverse_movie[row],reverse_user[col], nd.dot(U1[row,:],V1[:,col]))

    # Test on difficult distribution that ephasizes non-rated pairs where movies and users
    # are chosen based on rating count.
    neg_filename = "validation.hard.rndpairs.predictions";
    outfile = open(neg_filename,"w")
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
        if (row,col) in valid_hash:
            continue
        #print "shape,row,col", A.shape,row,col
        # if (A[row][col] > 0):
        #     continue
        print >> outfile, "%s,%s,%0.2f" % (reverse_movie[row],reverse_user[col], nd.dot(U1[row,:],V1[:,col]))

    outfile.close()

    ratings = {}
    predictions = []
    ratings_list = []

    outfile = open("test.predictions","w")

    train_files.extend(validation_files)
    (A,movie_ids,user_ids,m_count,u_count) = read_data_from_files(train_files,movie_ids,user_ids,m_count,u_count,discard=False)

    reverse_user = inverse_map(user_ids)
    reverse_movie = inverse_map(movie_ids)

    # Do nnmf
    (U1,V1) = hack_nmf_iter(A,k,.07,16*A.nnz,hard)

    for fname in test_files:
        f = open(fname)
        for line in f:
            fields = line.strip().split(",")
            movie_id = fields[0]
            user_id = fields[1]

            if movie_id in movie_ids and user_id in user_ids:
                row = movie_ids[movie_id]
                col = user_ids[user_id]
                ratings[(row,col)] =  1.0 #float(fields[2])
                ratings_list.append((row,col))
                prediction = nd.dot(U1[row,:],V1[:,col])
            else:
                # bayes prediction makes negative features be actual probabilities.
                #  that it outputs .07 in this case.
                ratings_list.append((movie_id,user_id))
                prediction = - .07
            predictions.append(prediction)
            print >> outfile, "%s,%s,%0.2f" % (movie_id,user_id, prediction)

    outfile.close()


    print "N ones", len(predictions)
    count = 0
    tries = 0
    ones_length = len(predictions)
    outfile = open("test.hard.rndpairs.predictions","w")
    if add_zeros:
        while count <= 12*ones_length and tries <= 100*ones_length:
            tries +=1
            j = random.randint(0,ones_length-1)
            if predictions[j] < 0:
                continue
            row = ratings_list[j][0]
            j = random.randint(0,ones_length-1)
            if predictions[j] < 0:
                continue
            col = ratings_list[j][1]
            if (row,col) in ratings:
                continue;
            count +=1
            ratings[(row,col)] = 0.0
            ratings_list.append((row,col))
            prediction = nd.dot(U1[row,:],V1[:,col])
            predictions.append(prediction)
            print >> outfile, "%s,%s,%0.2f" % (reverse_movie[row],reverse_user[col], nd.dot(U1[row,:],V1[:,col]))

    outfile.close()

    print "Total test", len(predictions)

    bayes_prediction = bayes_from_test_rndpairs(predictions,validation_filename,neg_filename,pos_prior=.1,min_x=0.0,max_x = 2.0,n_bins=20)

    mse = 0.0
    z_mse = 0.0
    mid_mse = 0.0

    count = 0
    for i in xrange(len(bayes_prediction)):
        pair = ratings_list[i]
        if (predictions[i] < 0):
            data = 1.0
        else:
            data = ratings[pair]
        if data > 1.0:
            print "data mistake? ", data, pair
        pred = bayes_prediction[i]
        diff = (pred - data)
        count +=1 
        mse += diff*diff
        z_mse += data*data
        mid_mse +=  (data-.07)**2

    print "rmse %f", math.sqrt(mse/count)
    print "zero rmse %f", math.sqrt(z_mse/count)
    print "mid rmse %f", math.sqrt(mid_mse/count)


# driver_movie_data_validate_bayes(train_files = glob.glob("data_sample/by_month_dir/2004-10.100K.sample.txt"),
#                                  validation_files = glob.glob("data_sample/by_month_dir/2004-11.100K.sample.txt"),
#                                  test_files =glob.glob("data_sample/by_month_dir/2004-12.100K.sample.txt"),
#                                  add_zeros =True)


driver_movie_data_validate_bayes(train_files = glob.glob("data_sample/by_month_dir/2004-10.100K.sample.txt"),
                                 validation_files = glob.glob("data_sample/by_month_dir/2004-11.100K.sample.txt"),

                                 test_files =glob.glob("data_sample/by_month_dir/2004-12.100K.sample.txt"),
                                 add_zeros =True,k=20,hard=True)
