import sys, csv, math
""" Calculate prediction based on global effects
    Input: Validation set, global effects set
    Output: movie, user, probability the pair exists in 2006 """
user_dic = {}
movie_dic = {}
def load_global_effects(filename):
    with open(filename, "rb") as csvfile:
        reader = csv.reader(csvfile, delimiter = '\t')
        for row in reader:
            if row[0] == 'movie_avg':
                movie_dic[row[1]] = row[2]
            else:
                user_dic[row[1]] = row[2]

def make_prediction(user, movie):
    population_rate = (100480507/float(480189*17750))
    user_adjusted_rate = float(user_dic[user])
    movie_adjusted_rate = float(movie_dic[movie])
    # prediction can be changed to include or exclude user/movie rates
    prediction = population_rate + user_adjusted_rate + movie_adjusted_rate
    if prediction < 0:
        prediction = 0
    return prediction
# global_effects is generated from the baseline/movie_total and user_total code
global_effects_set = 'global_effects_set.txt'
load_global_effects(global_effects_set)
RMSE = 0
count = 0
for line in sys.stdin:
    user, movie, answer = line.strip().split(',', 2)
    prediction = make_prediction(user, movie)
    if int(answer) > 0:
        answer = 1
    RMSE += (int(answer) - prediction)**2
    count += 1
    print '%s\t%s\t%s\t%s' % (user, movie, answer, prediction)
print math.sqrt(RMSE/float(count))
