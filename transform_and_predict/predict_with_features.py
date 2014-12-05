import sys
import os

sys.path.append('../nmf/')
sys.path.append('../classify/')

from some_tools import *
import transformation as trans

all_pos_feature_files = [
    ["answer_features/cluster.features.w.degree.scaled",
     "validation_sets_features/setA.a.nmf.predictions.scaled",
     "validation_sets_features/setA.b.nmf.predictions.scaled",
     "validation_sets_features/setB.a.nmf.predictions.scaled",
     "validation_sets_features/setB.b.nmf.predictions.scaled"]
    ,
    ["answer_features/who_rated_what_2006_global_predictions_fixed.txt",
     "validation_sets_features/setA.a.time.fixed",
     "validation_sets_features/setA.b.time.fixed",
     "validation_sets_features/setB.a.time.fixed",
     "validation_sets_features/setB.b.time.fixed"]
    ,
    ["answer_features/cos_feature.full_2006.fast.test.predictions.scaled",
     "validation_sets_features/setA.a.cos.test.predictions.scaled",
     "validation_sets_features/setA.b.cos.test.predictions.scaled",
     "validation_sets_features/setB.a.cos.test.predictions.scaled",
     "validation_sets_features/setB.b.cos.test.predictions.scaled"]
    ]

#all_feature_files = [all_pos_feature_files[0],all_pos_feature_files[1]]
#print "cluster and time"

# all_feature_files = [all_pos_feature_files[0],all_pos_feature_files[2]]
# print "cluster and cos"

#all_feature_files = [all_pos_feature_files[0]]
#print "cluster"

#all_feature_files = [all_pos_feature_files[2]]
#print "cos"

# all_feature_files = [all_pos_feature_files[1]]
# print "time"

# all_feature_files = [all_pos_feature_files[1],all_pos_feature_files[2]]
# print "cos and time"

all_feature_files = all_pos_feature_files
print "all features"

regression_info = ["validation_sets_features/setB.a","validation_sets_features/setB.b","answer_features/KDD_2007_who_rated_what.fixed.txt",
                   "this.is.outfile.name"]


validation_feature_files = []
answer_feature_files = []

for feature_file_info in all_feature_files:
    # Use distributions
    pos_dist_file = feature_file_info[1]
    neg_dist_file = feature_file_info[2]

    # to transform features in these files
    answer_set = feature_file_info[0]
    pos_validation_file = feature_file_info[3]
    neg_validation_file = feature_file_info[4]
    
    for fname in [answer_set,pos_validation_file,neg_validation_file]:
        trans.transform_features(fname,pos_dist_file,neg_dist_file, outfile_name =fname+".transformed")

    validation_feature_fname = pos_dist_file + ".and.neg"
        
    cmd = "cat " + pos_validation_file +".transformed " + neg_validation_file + ".transformed > " + validation_feature_fname
    answer_feature_files.append(answer_set+".transformed")
    validation_feature_files.append(validation_feature_fname)
    print "Issueing Cmd: ", cmd
    
    os.system(cmd)

validation_answer_fname = "temp/validation.answers.txt"
format_data(regression_info[0],regression_info[1],validation_answer_fname)


import logistic as log

model = log.train_logistic_model(validation_feature_files, validation_answer_fname) 

prediction_file = regression_info[3]

# print "answer file(s)"
# print answer_feature_files
# for fname in answer_feature_files:
#     os.system("tail " + fname)


log.predict_logistic_model(model, regression_info[2],
                           answer_feature_files, 
                           outfile_name=prediction_file,
                           correct_imbalance = .14)

# print "prediction file"
# print prediction_file
# os.system("tail " + fname)

compute_rmse(prediction_file, regression_info[2])


