import numpy as np
from sklearn.linear_model import LogisticRegression

def train_logistic_model(feature_files,test_pair_filename):

    y = []
    cnt = 0
    pairs_to_index = {}
    pair_file = open(test_pair_filename)
    for line in pair_file:
        fields = line.strip().split(",")
        pairs_to_index[(fields[0],fields[1])] = cnt
        cnt+=1
        y.append(float(fields[2]))

    n_features = len(feature_files)
    n_samples = cnt
    
    X  = np.zeros((n_samples,n_features))

    feature_no = 0
    for feature_file in feature_files:
        this_file = open(feature_file)

        for line in this_file:
            fields = line.strip().split(",")
            movie = fields[0]
            user = fields[1]
            if (movie,user) in pairs_to_index:
                sample_index = pairs_to_index[(movie,user)]
                X[sample_index,feature_no] = float(fields[2])

        feature_no+=1


    logistic_model = LogisticRegression()

    logistic_model.fit(X,y)
    
    return logistic_model


def predict_logistic_model(logistic_model,predict_pairs_file,
                           feature_files,outfile_name="./prediction",correct_imbalance=1.0):
    cnt = 0
    pairs_to_index = {}

    pair_file = open(predict_pairs_file)
    for line in pair_file:
        fields = line.strip().split(",")
        #print fields
        pairs_to_index[(fields[0],fields[1])] = cnt
        cnt+=1

    pair_file.close()
    n_features = len(feature_files)
    n_samples = cnt
    
    X  = np.zeros((n_samples,n_features))

    feature_no = 0
    for feature_file in feature_files:
        this_file = open(feature_file)

        for line in this_file:
            fields = line.strip().split(",")
            movie = fields[0]
            user = fields[1]
            if (movie,user) in pairs_to_index:
                sample_index = pairs_to_index[(movie,user)]
                X[sample_index,feature_no] = float(fields[2])

        feature_no+=1

    y = logistic_model.predict_proba(X)

    outfile = open(outfile_name, "w")
    for (movie,user) in pairs_to_index.keys():
        index = pairs_to_index[(movie,user)]
        print >> outfile, "%s,%s, %f" % (movie,user,correct_imbalance*y[index][1])
        
    outfile.close()



    
        
