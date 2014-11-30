import numpy as np
import csv
#import matplotlib.pyplot as plt

def read_dist(filename,bins = 15,range=(0,2)):
    b = csv.reader(open(filename))
    pts = []

    for data in b:
        #print "data", data
        x = float(data[2])
        if (x > 2.0):
            x = 1.999
        elif x < 0:
            x = 0.001
        pts.append(x)

    return(np.histogram(np.array(pts),bins=bins,range=range,density=True))

def find_bin(prediction, min_x,max_x,n_bins):
    if (prediction >= max_x):
        return n_bins-1
    return (int(n_bins*(prediction-min_x)/(max_x-min_x)))

def bayes_from_test_rndpairs(predictions,pos_dist_file,neg_dist_file,pos_prior=.5,min_x=0.0,max_x = 2.0,n_bins=20):
    bins =[]
    for i in xrange(0,20):
        bins.append(i*((max_x - min_x)/n_bins))

    (pos_density,pos_bins) = read_dist(pos_dist_file,bins=bins,range=(min_x,max_x))
    (neg_density,neg_bins) = read_dist(neg_dist_file,bins=bins,range=(min_x,max_x))
    
    neg_prior = 1.0 - pos_prior
    print "pos_density", pos_density
    print "neg_density", neg_density
    
    width = (max_x-min_x)/n_bins

    result = []
    for prediction in predictions:

        if prediction < 0:
            # negative numbers signal that
            # we pass through the absolute value
            # as probability bypassing this
            # calculation
            result.append(-prediction)
            continue

        b = find_bin(prediction,min_x,max_x,n_bins)
        if (b >= min(len(pos_bins),len(neg_bins)) -1):
            print "fixing b", b
            b = min(len(pos_bins),len(neg_bins))-2
        elif (b < 0):
            print "fixing b", b
            b = 0
        #print b
        pred_and_POS = pos_density[b]*width* pos_prior
        pred_and_NEG = neg_density[b]*width* neg_prior
        #print pred_and_POS
        #print pred_and_NEG
        if (pred_and_POS + pred_and_NEG < .00001):
            result.append(pos_prior)
        else:
            result.append(pred_and_POS/(pred_and_POS + pred_and_NEG))

    return result
