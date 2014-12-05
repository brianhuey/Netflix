generate_sets.py - Used to create validation sets similar to test set!
concat.py- Used to load all 17,000 movie files into one large file, training set for work on EC2. 


To generate validation sets in python call generate_sets('./validationSetA', post2005_training.txt, pre2005_training.txt) after retrieving the two files from s3.

(Both files are available in s3/stat157-uq85def/shared/netflix/training2)


To generate the full training set with ratings including 2005 run python concat.py >> training_set.txt after downloading the pre and post 2005 data from s3.
