

Feature: NMF
This is the code we used to compute our NMF features. It is quite slow, and probably best to run on  an EC2 instance. 

To compute the features for a set of data:





Graphs:
To run do.nmf.graphs.R which show distribution of features on ratings and non-ratings of validation setA to 
assess feature utility:

In R run source("do.nmf.graphs.R") after moving the files setA.a.nmf.validation.scaled and 
setA.b.nmf.test.validation.scaled to this directory from s3/stat157-uq85def/home/reneerao/Data 
for Netflix project.

