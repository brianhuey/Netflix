
import glob
import shutil
import os

filenames = glob.glob("training_set/mv_*.txt")

if (len(glob.glob("training_set_w_mid")) > 0):
    shutil.rmtree("training_set_w_mid")
os.mkdir("training_set_w_mid")

for fname in filenames:
    fname_base = fname.split("/")[1]
    new_name =  "training_set_w_mid" + "/" + fname_base
    out_file = open(new_name,"w")
    this_file = open(fname)
    movie_id = this_file.readline().strip()[0:-1]
    for x in this_file:
        out_file.write(movie_id)
        out_file.write(",")
        out_file.write(x)

        
                        


