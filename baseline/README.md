Baseline calculations
===============
Author: Brian Huey
Global effects calculations as described in Bell, Koren
http://www.cs.uic.edu/~liub/KDD-cup-2007/proceedings/Neighbor-Koren.pdf

<h2>Structure:</h2>
<br>/join_avgs - MapReduce joins. Takes training data and sequentially appends movie_total, user_total
<br>/movie_total - probability of rating for a given movieid (total number ratings of movie/total number of movies)
<br>/movie_sqrt_time - square root of time since movie was first rated
<br>/movie_center_time - centers the sqrt of time since movie first rated around the mean for the movie
<br>/movie_time_coefficients - produces the movie time coefficient that estimates effect time has on rating probability
<br>/user_total - probability of rating for a given userid (total number ratings by a user/total number of users)
<br>/user_sqrt_time - square root of time since user first rated a movie
<br>/user_center_time - centers the sqrt of time since user first rated around the mean for the user
<br>/user_time_coefficients - produces the user time coefficient that estimates effect time has on rating probability
<br>append_global_effect.py - loads the movie avg, user avg, movie time and user time coefficient files and appends the final calculation to a set.
<br> Extra utilities:
<br>/sqrt_time - extra sqrt time code, not used
<br>/time_coefficient - extra time coefficient code, not used
<br>/total - calculates total ratings for validation purposes

<h2>Workflow:</h2>
<br> Within each directory there should be a mapper and reducer. Each step assumes the user runs both.
<br>1) /movie_total and /user_total are run, the output is fed in to movie_averages.py and user_averages.py to generate movie_averages.txt and user_averages.txt
<br>2) training data, user_averages.txt, movie_averages.txt are inputs to the mapper and reducer in /join_avgs
<br>3) /joins is an input to /movie_sqrt_time
<br>4) /movie_time_sqrt_time is an input to /movie_center_time
<br>5) /movie_center_time is an input to /user_sqrt_time
<br>6) /user_sqrt_time is an input to /user_center_time
<br>7) /user_center_time is an input to /movie_time_coefficient and /user_time_coefficient which generates movie_coeff.txt and user_coeff.txt respectively.
<br>8) Run append_global_effect.py to attach the global affect feature to the validation/test set.
