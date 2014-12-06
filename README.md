Netflix-project
===============
We are working the Netflix dataset used in the 2007 KDD Cup competition which provides information on characteristics of users of the Netflix video services who left ratings for movies from the years 1998 to 2004 (http://www.kdd.org/kdd-cup-2007-consumer-recommendations).

<h2>Structure:</h2>
<br>/baseline - map/reduce jobs used to create global effects features and append them to the validation/test set. Graphs of feature.
<br>/reports - report documentation. Herein lies our final report.
<br>/transform_and_predict - Transforms features, fits logistic model, makes predictions and computes RMSE with the answer set from 2006 
<br>/data_manipulation - various operations to produce validation sets and format data
<br>/training_set_sample - map/reduce jobs used to subset and sample the training set.
<br>/nmf - Create and run non-negative matrix factorization alogrithm. Graph of feature.
<br>/cosine - Create and run cosine simiarlity alogrithm. Graphs of feature.
