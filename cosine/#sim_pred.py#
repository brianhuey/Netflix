#from nmfplus import *
import random
import numpy as np
import scipy.sparse as sp
import math

# Computes the average cosine similarity between movie vector and all user neighbor movies

def predict_with_similarity(user,movie,At,A,cosine_sim=False):
    if ((user >= At.shape[0]) or (movie >= At.shape[1])):
        return(0.0,0.0)
    
    raw = A.getrow(movie)
    movie_neighbors = raw.transpose()
    if cosine_sim:
        mag_movie = math.sqrt(raw.dot(movie_neighbors)[0,0])

    val = 0
    #     print At.shape
    #     print user,movie
    for row_col_index in xrange(At.indptr[user],At.indptr[user+1]):
        rated_movie = At.indices[row_col_index]

        rated_movie_neighbors = A.getrow(rated_movie)

        if cosine_sim:
            mag_rated_movie = math.sqrt(rated_movie_neighbors.dot(rated_movie_neighbors.transpose())[0,0])

        score = rated_movie_neighbors.dot(movie_neighbors)[0,0]/(mag_rated_movie*mag_movie)
        #         print "score", score
        #         print rated_movie,movie
        #         print rated_movie_neighbors
        #         print "movie_neighbors"
        #         print movie_neighbors

        val += score
        #print "val", val
        
    return (val,At.indptr[user+1]-At.indptr[user])

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

# Helper function to get back original user, movie_ids
def inverse_map(the_mapping):
    reverse_mapping = {}
    for key in the_mapping.keys():
        reverse_mapping[the_mapping[key]] = key
    return reverse_mapping


def final_similarity_prediction(filename,test_filename,dir_prefix="./similarity.", cosine_sim=False):

    outfile = open(dir_prefix+"test.predictions","w")

    (A,movie_ids,user_ids,m_count,u_count) = read_data(filename)

    reverse_user = inverse_map(user_ids)
    reverse_movie = inverse_map(movie_ids)
    At = A.transpose()
    
    
    trainA = A
    train_m_count = m_count
    train_u_count = u_count
    At = At.tocsr()

    (A,movie_ids,user_ids,m_count,u_count) = read_data(test_filename,movie_ids,user_ids,m_count,u_count,discard=True)

    print ("Total of %d test ratings" % A.nnz)
    (n,m) = A.shape
    cnt=0


    print_int = 100
    for i in xrange(A.nnz)):
        movie = find_index(A.indptr,i)            
        user = A.indices[i]
        (val1,deg) = predict_with_similarity(user,movie,At,trainA,cosine_sim)
        cnt+=1
        if (cnt%print_int == 0):
            print "cnt,movie,user,deg,val1", cnt, row,col,deg,val1
        print >> outfile, "%s,%s,%0.5f,%0.5f" % (reverse_movie[movie],reverse_user[user], val1,deg)
        
    outfile.close()


