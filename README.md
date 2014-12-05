Netflix-project
===============
We are working the Netflix dataset used in the 2007 KDD Cup competition which provides information on characteristics of users of the Netflix video services who left ratings for movies from the years 1998 to 2004 (http://www.kdd.org/kdd-cup-2007-consumer-recommendations).

<h2>Structure:</h2>
<br>/baseline - map/reduce jobs used to create global effects features and append them to the validation/test set.
<br>/reports - report documentation
<br>/nmf - Non-negative matrix factorization algorithm
<br>/data_sample - Data sets sampled from the original KDD data
<br>/training_set_sample - map/reduce jobs used to subset and sample the training set.
<br>/training_set_with_movie_ids - Code to reshape training data in to usable format (movie, user, rating, date)
<br>/nmf - Create and run non-negative matrix factorization alogrithm
