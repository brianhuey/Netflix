Baseline calculations
===============
Global effects calculations as described in Bell, Koren
http://www.cs.uic.edu/~liub/KDD-cup-2007/proceedings/Neighbor-Koren.pdf

<h2>Structure:</h2>
<br>/movie_total - probability of rating for a given movieid (total number ratings of movie/total number of movies)
<br>/movie_time - square root of time since movie was first rated
<br>/user_total - probability of rating for a given userid (total number ratings by a user/total number of users)
<br>/user_time - square root of time since user first rated a movie
<br>/joins - MapReduce joins. Takes training data and sequentially appends movie_total, user_total
<br>/time_coefficients - estimated time effects
<br>/total - calculates total ratings for validation purposes
<br>/counts - simple counting tools for validation purposes

The workflow is as follows:
1) movie_total and user_total used to generate movie_averages.txt and user_averages.txt
2) training data, user_averages.txt, movie_averages.txt are inputs to the mapper and reducer in /joins
3) /joins is an input to /movie_time/sqrt_time
4) /movie_time/movie_sqrt_time is an input to /movie_time/movie_center_time
5) /movie_time/movie_center_time is an input to /user_time/user_sqrt_time
6) /user_time/user_sqrt_time is an input to /user_time/user_center_time
7) /user_time/user_center_time is an input to /time_coefficients/movie_time_coefficient_only and /time_coefficients/user_time_coefficient_only which generates movie_coeff.txt and user_coeff.txt respectively.
