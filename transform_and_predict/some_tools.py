import sys

sys.path.append('../nmf/')
sys.path.append('../classify/')

import logistic as log
import math

# Translates .tsv to .csv (used on Brian's time data)
def tab_to_comma(filename1,outfile_name):
    
    f1 = open(filename1)

    outfile = open(outfile_name, 'w')

    for line in f1:
        fields = line.strip().split('\t')
        
        print >> outfile, '%s,%s,%s' % (fields[0],fields[1],fields[2])

# Ensures all data is in the format we want it in!
def format_data(filename1,filename2,outfile_name):
    
    f1 = open(filename1)
    f2 = open(filename2)
    outfile = open(outfile_name, 'w')
    
    for line in f1:
        fields = line.strip().split(',')
        
        print >> outfile, '%s,%s' % (fields[0],fields[1]) + ",1"

    for line in f2:
        line = line.strip()
        fields = line.strip().split(',')

        print >> outfile, '%s,%s' % (fields[0],fields[1]) + ",0"
    outfile.close()

#format_data("setB.a.time.fixed", "setB.b.time.fixed", './logistic.test.time')


# Computes the RMSE between predictions and test file. 
def compute_rmse(prediction_file, test_file):
    
    f1 = open(prediction_file)
    f2 = open(test_file)
    
    predic_dict = {}
    test_dict = {}

    for line in f1:
        fields = line.strip().split(',')
        val = float(fields[2])
        if abs(val) > 1.0:
# We should never get here
            print line
            print "WTF"
        predic_dict[(fields[0],fields[1])] = val

    for line in f2:
        fields = line.strip().split(',')
        if int(fields[2]) == 0:
            test_dict[(fields[0],fields[1])] = 0.0
        else:
            test_dict[(fields[0],fields[1])] = 1.0

    se = 0.0
    zse = 0.0
    fse = 0.07
    count = 0.0
    for key in predic_dict:
        se = se + ((predic_dict[key])-(test_dict[key]))**2
        zse = zse + ((test_dict[key]))**2
        fse = fse + ((test_dict[key])-0.07)**2
        count += 1
    
# Returns RMSE for our predictions, predicting all 0's or predicting all .07 the baseline probability of being rated. 
    print "zero rmse",  math.sqrt(zse/count)
    print ".07 rmse",  math.sqrt(fse/count)
    rmse = math.sqrt(se/count)
    print "predict rmse", rmse
    return rmse

#compute_rmse('./prediction.time', 'KDD_2007_who_rated_what.txt')
