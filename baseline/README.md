Baseline calculations
===============
Global effects calculations as described in Bell, Koren
http://www.cs.uic.edu/~liub/KDD-cup-2007/proceedings/Neighbor-Koren.pdf

<h2>Structure:</h2>
<br>/movie_total - probability of rating for a given movieid (total number ratings of movie/total number of movies)
<br>/movie_time - square root of time since movie was last rated
<br>/user_total - probability of rating for a given userid (total number ratings by a user/total number of users)
<br>/user_time - square root of time since user last rated a movie
<br>/joins - MapReduce joins. Takes training data and sequentially appends movie_total, user_total, movie_time and user_time.
