import random
import numpy as np
import scipy.sparse as sp
import math

# Used to generate validation sets of known ratings and popularity distributed, unrated random movie-user pairs




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

def inverse_map(the_mapping):
    reverse_mapping = {}
    for key in the_mapping.keys():
        reverse_mapping[the_mapping[key]] = key
    return reverse_mapping

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


def generate_sets(outfile_prefix,validation_set,train_set,n_samples=10000,print_int = 100):

    (trainA,movie_ids,user_ids,m_train_count,u_train_count) = read_data(train_set)

    (A,movie_ids,user_ids,m_count,u_count) = read_data(validation_set,movie_ids,user_ids,m_train_count,u_train_count)

    reverse_user = inverse_map(user_ids)
    reverse_movie = inverse_map(movie_ids)

    outfile = open(outfile_prefix + ".a","w")

    cnt = 0

    for row in xrange(min(n_samples,A.nnz)):
        i = random.randint(0,A.nnz -1)
        row = find_index(A.indptr,i)            
        col = A.indices[i]
        cnt+=1
        if (cnt%print_int == 0):
            print "cnt,movie,user,deg,val1", cnt, row,col
        print >> outfile, "%s,%s" % (reverse_movie[row],reverse_user[col])
        
    outfile.close()

    outfile = open(outfile_prefix + ".b","w")

    print ("Doing random difficult pairs")

    n_pairs = 0
    bailout = 10*n_samples
    while n_pairs < n_samples and bailout > 0:
        bailout-=1
        i = random.randint(0,A.nnz -1)
        row = find_index(A.indptr,i)
        j = random.randint(0,A.nnz -1)
        col = A.indices[j]
        if (A[row,col] > 0):
            continue
        if (row < m_train_count and col < u_train_count and trainA[row,col] > 0):
            continue
        cnt+=1
        n_pairs+=1
        if (cnt%print_int == 0):
            print "cnt,movie,user,deg,val1", cnt, row,col
        print >> outfile, "%s,%s"  % (reverse_movie[row],reverse_user[col])

    outfile.close()
