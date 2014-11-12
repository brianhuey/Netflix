Netflix-project
===============
We are working the Netflix dataset used in the 2007 KDD Cup competition which provides information on characteristics of users of the Netflix video services who left ratings for movies from the years 1998 to 2004 (http://www.kdd.org/kdd-cup-2007-consumer-recommendations).

Structure:
/baseline - Random sampling code, MapReduce code for calculating global effects for user and movie groups
/data - This is where the KDD data goes, ignored on the remote repository
/data_sample - Data sets sampled from the original KDD data
/make_predictions - Make predictions and compute RMSE against test set
/training_set_sample - Data sets sampled from original KDD training set
/training_set_with_movie_ids - Code to reshape training data in to usable format (movie, user, rating, date)