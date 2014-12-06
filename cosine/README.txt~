To compute cos similarity for the validation sets, and run final_similarity_predictions in python, varying the inputs (datafiles from S3) accordingly.


To get cos similarity features on validation setA.a (or setA.b,setB.a,setB.b):

inputs: filename = 'pre_2005.training', (available at s3/stat157-uq85def/shared/netflix/training2/pre_2005.training) 
   	test_filename = 'setA.a', (avaiable at s3/stat157-uq85def/shared/netflix/feature_sample/setA.a
	dir_prefix ='./setA.a.cos.validation'
	cosine_sim = True
	
To get cos similarity features on test set 2006:

inputs:
	filename ='training_set.txt' (available at s3/stat157-uq85def/shared/netflix/training2/training_set.txt)
	test_filename = 'who_rated_what_2006.txt' (available at s3/stat157-uq85def/shared/netflix/test_sets/who_rated_what_2006.txt')
	dir_prefix = './who_rated_what_2006.cos.test'
	cosine_sim=True



To run do.cos.graphs.R which show distribution of features on ratings and non-ratings of validation setA to assess feature utility:

In R run source("do.cos.graphs") after moving the files setA.a.cos.test.predictions.scaled and setA.b.cos.test.predictions.scaled to this directory from s3/stat157-uq85def/home/reneerao/Data for Netflix project.



