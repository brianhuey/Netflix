import numpy as np
import csv

def read_dist(filename,bins = 15,prune=.05,max_val=False,min_val=False):
    b = open(filename)
    print filename
    pts = []
    for line in b:
        #print line
        data = line.strip().split(",") 
        #print "data", data
        x = float(data[2])
        pts.append(x)

    b.close()
    pts.sort()
    n = len(pts)
    
    if (not max_val):
        max_val = pts[int((1.0-prune)*n)]
    if (not min_val):
        min_val = pts[int((prune)*n)]

    for i in xrange(n):
        pts[i] = min (max_val,pts[i])
        pts[i] = max (min_val,pts[i])

    
    return(pts,min_val,max_val)

def find_bin(prediction, min_x,max_x,n_bins):
    if (prediction >= max_x):
        return n_bins-1
    return (int(n_bins*(prediction-min_x)/(max_x-min_x)))


def transform_features(test_feature_file, pos_dist_file, neg_dist_file, outfile_name='./transformed.features', pos_prior=.07, tail_prune = .05,n_bins=20):
    

    (pos_pts,min_val,max_val) = read_dist(pos_dist_file,bins=n_bins,prune=tail_prune)
    (neg_pts,min_val,max_val) = read_dist(neg_dist_file,bins=n_bins,prune=tail_prune,max_val=max_val,min_val=min_val)

    print "min,max", min_val,max_val

    (pos_density,pos_bins) = np.histogram(np.array(pos_pts),bins=n_bins,range=(min_val,max_val),density=False)
    (neg_density,neg_bins) = np.histogram(np.array(neg_pts),bins=n_bins,range=(min_val,max_val),density=False)
    
    neg_prior = 1.0 - pos_prior
    print "pos_density", pos_density
    print "neg_density", neg_density
    
    width = (max_val-min_val)/n_bins

    result = []
    
    f = open(test_feature_file)
    
    outfile = open(outfile_name, "w")

    for line in f:
        fields = line.strip().split(',')
        prediction = float(fields[2])

        
        b = find_bin(prediction,min_val,max_val,n_bins)
        if (b >= min(len(pos_bins),len(neg_bins)) -1):
            #print "fixing b", b
            b = min(len(pos_bins),len(neg_bins))-2
        elif (b < 0):
            #print "fixing b", b
            b = 0
        #print b
        pred_and_POS = pos_density[b]* pos_prior
        pred_and_NEG = neg_density[b]* neg_prior
        #print pred_and_POS
        #print pred_and_NEG
        if (pred_and_POS + pred_and_NEG < .00001):
            print >> outfile, "%s,%s,%f" % (fields[0],fields[1], pos_prior)
        else:
            print >> outfile, "%s,%s,%f" % (fields[0],fields[1],(pred_and_POS/(pred_and_POS + pred_and_NEG)))

    outfile.close()
