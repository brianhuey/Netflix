
def switch_movie_user(filename):
    
    f = open(filename)
    
    for line in f:
        fields = line.strip().split(",")

        print "%s,%s,%s" % (fields[1],fields[0],fields[2])


def convert_tab_to_comma(filename):
    
    f = open(filename)
    
    for line in f:
        fields = line.strip().split("\t")

        print "%s,%s,%s" % (fields[0],fields[1],fields[2])

#convert_tab_to_comma('./who_rated_what_2006_global_predictions.txt')
#convert_tab_to_comma('./setA.a.time')
#convert_tab_to_comma('./setB.b.time')

