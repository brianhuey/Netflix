import sys, csv, math, datetime
""" Calculate prediction based on global effects
    Input: Validation set, global effects set
    Output: movie, user, probability the pair exists in 2006 """
# Load movie averages
movie_dic = {}
with open('movie_averages.txt', "rb") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
        movie_avg = float(row[1])
        movie_dic[row[0]] = movie_avg
# Load user averages
user_dic = {}
with open('user_averages.txt', "rb") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
        user_avg = float(row[1])
        user_dic[row[0]] = user_avg
# Load movie time coefficients
movie_time_dic = {}
with open('movie_coefficients.txt', "rb") as csvfile:
    alpha = 1000
    reader = csv.reader(csvfile, delimiter = '\t')
    for row in reader:
        theta = float(row[1])
        N = int(row[2])
        movie_time_dic[row[0]] = (theta*N)/float(N+alpha)
# Load user time coefficients
user_time_dic = {}
with open('user_coefficients.txt', "rb") as csvfile:
    alpha = 1000
    reader = csv.reader(csvfile, delimiter = '\t')
    for row in reader:
        theta = float(row[1])
        N = int(row[2])
        user_time_dic[row[0]] = (theta*N)/float(N+alpha)
"""user_first_rated_dic = {}
with open('user_first_rated.txt', "rb") as csvfile:
    reader = csv.reader(csvfile, delimiter = '\t')
    for row in reader:
        first_date = datetime.datetime.strptime(row[1][0:10], '%Y-%m-%d')
        day_since = datetime.datetime.strptime('2005-01-01', '%Y-%m-%d') - first_date
        user_first_rated_dic[row[0]] = int(day_since.days)
movie_first_rated_dic = {}
with open('movie_first_rated.txt', "rb") as csvfile:
    reader = csv.reader(csvfile, delimiter = '\t')
    for row in reader:
        first_date = datetime.datetime.strptime(row[1][0:10], '%Y-%m-%d')
        day_since = datetime.datetime.strptime('2005-01-01', '%Y-%m-%d') - first_date
        movie_first_rated_dic[row[0]] = int(day_since.days)"""
def append_baseline(movie, user):
    if user not in user_time_dic:
        user_adjusted_rate = 0
        user_time_adjusted_rate = 0
    else:
        user_adjusted_rate = user_dic[user]
        user_time_adjusted_rate = user_time_dic[user]#*user_first_rated_dic[user]
    if movie not in movie_time_dic:
        movie_adjusted_rate = 0
        movie_time_adjusted_rate = 0
    else:
        movie_adjusted_rate = movie_dic[movie]
        movie_time_adjusted_rate = movie_time_dic[movie]#*movie_first_rated_dic[movie]
    total_movies = 17750 # Calculated
    total_users = 480189 # Calculated
    overall_rate = (100480507/float(total_movies * total_users))
    effect = (overall_rate + user_adjusted_rate + user_time_adjusted_rate
        + movie_adjusted_rate + movie_time_adjusted_rate)
    #print '%s\t%s\t%s\t%s\t%s\t%s' % (movie, user, user_adjusted_rate, user_time_adjusted_rate,
    #    movie_adjusted_rate, movie_time_adjusted_rate)
    print '%s\t%s\t%s' % (movie, user, effect)

for line in sys.stdin:
    movie, user = line.strip().split(',', 1)
    append_baseline(movie, user)
