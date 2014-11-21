import numpy as np
import csv
import math
from sklearn.decomposition import ProjectedGradientNMF
import scipy.sparse as sparse

def read_data(filename, movie_ids={}, user_ids={}, n_movies=0, n_users=0):
    row = []
    column = []
    values = []
    f = open(filename)
    for line in f:
        fields = line.strip().split(",")
        movie_id = fields[0]
        user_id = fields[1]

        if not movie_id in movie_ids:
            movie_ids[movie_id] = n_movies
            n_movies +=1
        if not user_id in user_ids:
            user_ids[user_id] = n_users
            n_users += 1

        row.append(movie_ids[movie_id])
        column.append(user_ids[user_id])
        values.append(1.0)

    return sparse.csr_matrix((values,(row,column)),shape=(n_movies,n_users))

iterations = 200

def nmf(matrix, k):
    A = matrix
    model = ProjectedGradientNMF(n_components=k, init='nndsvd', sparseness = None,
                                random_state=0, max_iter = iterations)
    model.fit(A)
    W = model.fit_transform(A)
    H = model.components_
    print W.

def rmse(training_set, W, H):
    training = training_set
    n,m = training.shape
    rmse = 0.0
    se = 0.0
    count = 0
    index_hash = {}
    for row in xrange(n):
        for row_col_index in xrange(training.indptr[row],training.indptr[row+1]):
            col = training.indices[row_col_index]
            elt = training.data[row_col_index]
            index_hash[(row,col)] = True
            diff = elt - np.dot(W[row,:],H[:,col])
            se += diff**2
            count += 1
    rmse = math.sqrt(se/float(count))
    print rmse


training = read_data("../data/sample.100K.train.txt")
W, H = nmf(training, 5)
rmse = rmse(training, W, H)
