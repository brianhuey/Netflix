"""
The pipeline is as follows:

1. Make features from pre.2005 data.

    Examples:
        1) non-negative matrix factorization 
        2) user-movie naive bayes statistics

    Note:
       cosine similarity feature needs no preprocessing.

2. Validate features using 2005 data.

   Compute feature distributions for

      a) random subset rated user,movie pairs in 2005
      b) popularity distributed random subset of unrated user,movie pairs from 2005
      c) uniform random subset of unrated user,movie pairs in 2005

   Note that this entails computing features for 2005 pairs, which 
   may use precomputation from pre 2005 data or just use the data.
   For example, cosine similarity for (user,movie) computes
   the cosine similarity of "movie" with all other movies
   rated by user pre.2005 using pre.2005 data.

3. Transform features to probabilities using distributions.

     Transform features into probabilities using Bayes rule
     with the positive(rated)/negative(unrated) distributions
     from above.
   
     We will run 2 experiments:

        (1) one to distinguish rated movies from uniformly random unrated movies
            in which case we use the uniformly random movies as the negative
            distribution.
        (2) one to distinguish rated movies from proportionally sampled unrated movies
            in which case we use the proportionally sample movies as the negative
            distribution.

4.  Combine features and predict.

     Prediction Algoirithm on transformed features.

    Method 1: Naive Bayes.
       Compute features for answer set using all pre.2006 data.  
       Transform features using part (2) transformation.
    
       Predict using Naive Bayes.

    Method 2:
        Compute features for all pre.2005 data.  
        Transform features using part (2) transformations.
        Combine using Naive Bayes into Super Feature

        Compute part(2) supertransformation transformation for super feature.
       
        Compute Transformed features for answer set using all pre.2006 data.
        Combine using Naive Bayes into Super Feature
        Apply supertransformation as prediction.

"""

"""
Implementation Strategy.

DATA SET:

Generate two sets of "validation pairs"

a) rated pairs from 2005
b) unrated pairs from popularity proportional distribution in 2005
c) unrated pairs from uniform distribution in 2005


Set A and Set B
---

FEATURE FITTING AND COMBINATION

For each feature, generate values for Set A, (a),(b),(c)

For each feature, generate transformed values for Set B (a) (b) (c) using pos/neg distributions
for set A. (a) is pos (c) is neg    (We could do (a) and (b) against easy distribution.)


foreach feature do the following:
  transform(feature_file_for_B_a, feature_file_for_A_a,feature_file_for_A_b, outfile="transform.feature.B.a")
  transform(feature_file_for_B_b, feature_file_for_A_a,feature_file_for_A_b, outfile="transform.feature.B.b")
  transform(feature_file_for_B_c, feature_file_for_A_a,feature_file_for_A_c, outfile="transform.feature.B.c")


  naive_bayes_combine(all_features, "B.a", outfile="naive.bayes.combined.B.a")
  naive_bayes_combine(all_features, "B.b", outfile="naive.bayes.combined.B.b")
  naive_bayes_combine(all_features, "B.c", outfile="naive.bayes.combined.B.c")




Naive Bayes combine the features using Set B transformed features.
Compute naive bayes feature for Set (B) (a) (b) (c)
Generate transformation for this feature.

-------

PREDICTION

For each feature generate values for answer set
trained on all data, transformed using transformers
from above.

Combine using naive bayes, and naive bayes transformer
to generate predictions.

foreach feature:
   compute_feature(answer_set)
   transform_feature(answer_set, feature_file_for_A_a, feature_file_for_A_b...)

naive_bayes_combine(all_transformed_features_answer_set, outfile"naive.bayes.combined.answerset)
transform("naive.bayes.combined,answerset", feature_file_naive_for_B_a, feature_file_naive_for_B_b, outfile="final.predictions")!!!!

Evaluate.

check rmse on final prediction!

"""


""" 
Step 4.

"""

def naive_bayes_combine_features(feature_files,predict_pairs,output_prefix="./",default_values = False, default_value = .5):

    feature_hashs[]

    for (fname) in feature_files:
        this_feature_hash = {}
        f = open(fname)
        for line in feature_file:
            fields = line.strip().split(",")
            this_feature_hash[(fields[0],fields[1])] = float(fields[2])
            
        feature_hashs.append(this_feature_hash)
    
    outfile = open(output_prefix+".combined","w")
    
    for (movie,user) in predict_pairs:
        pair = (movie,user)
        value = 1.0
        i = 0
        for this_feature_hash in feature_hashs:
            if pair in this_feature_hash:
                value *= (1-this_feature_hash[pash])
            else:
                if default_values:
                    value *= default_values[i]
                else:
                    value *= default_value
        
            i+=1 

        print >> outfile, "%s, %s, %f" % (movie,user,value)



def fit_final(set_B_pairs, set_B_features,set_B_defaults,outfile_name=""):

    for subset in xrange(len(set_B_pairs)):



        
        






    
