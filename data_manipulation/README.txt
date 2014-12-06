Author Renee Rao

The following files were used to variously, sample, format and scale our data and features.

generate_sets.py - Used to create validation sets similar to test set!
concat.py- Used to load all 17,000 movie files into one large file, training set for work on EC2. 


To generate validation sets in python call generate_sets('./validationSetA', post2005_training.txt, pre2005_training.txt) after retrieving the two files from s3.

(Both files are available in s3/stat157-uq85def/shared/netflix/training2)


To generate the full training set with ratings including 2005 run python concat.py >> training_set.txt after downloading the pre and post 2005 data from s3.


fix_cos_sim.py,fix_KDD_answers.py,scale.py, and transform_time.py are all python scripts used at various points to format the data correctly, intended only to be used one time as a result of aprevious formatting errors.

fix_cos_sim - reformed cosine similarity feature output after outputing an incorect format on test set.

fix_KDD_answers.py - the order of the movie, user pair was switch in the original answer. This switches it back

scale.py - scales feature values for nmf and cosine similarity by fourth value.	Note this should be run on output of the nmf and cosine features before inputing them to the the transform and prediction method for better results.	

transform_time.py - turn '\t' separated	files into ',' separated files.	