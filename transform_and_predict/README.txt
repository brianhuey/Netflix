Author: Renee Rao 

To make predictions on the features from the test set download the validation_sets_features, answer_features and temp folders as well the KDD_2007_who_rated_what.txt from the s3 bucket s3/stat157-uq85def/home/reneerao/Data for Netflix project.

After doing so run python predict_with_features.py to get RMSE of predictions using all three features. You can tune which features you choose to include by chaining the inputs from within the predict_with_features.py file. 

some_tools.py, logistic.py and transformation.py are all called within the predict with features file. Tools is used to compute RMSE and format files if needed. Logistic is uses to get the sklearn logistic regression package to create a model and output predictions. Transformation is used to translate each feature value into probabilities using Bayes rule on the validation sets. 
