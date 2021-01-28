#Our goal will be to see if people really liked the movies that are suggested to them since the users have already rated some of the movies suggested


from data import ratings, movies, genre_cols,users
from functions import get_recommendations
from accessors import get_ratings_user, get_rating_movie_user


similarity_mat = movies[genre_cols].values.dot(movies[genre_cols].values.T)
users_ids = users['user_id'].tolist()

#Making sure everything is an integer
rated_average =[]
recommended_average=[]
i = 0
len_users = len(users_ids)
while i< len_users-1:
    users_ids[i]=int(users_ids[i])
    i=i+1


for user_id in users_ids:

    recom =get_recommendations(user_id,ratings,similarity_mat,movies)
    recommended_movies = recom['movie_id'].tolist()
    rated = get_ratings_user(ratings,user_id)
    rated_movies= rated['movie_id'].tolist()
    List_of_ratings = []
    for movie in recommended_movies:
        if movie in rated_movies:
            List_of_ratings.append(get_rating_movie_user(ratings,user_id,movie))

    #Making sure everything is an integer
    i=0
    length=len(List_of_ratings)

    while i < length-1:
        List_of_ratings[i] = int(List_of_ratings[i])
        i=i+1


    List_of_ratings_total=[]
    for movie in rated_movies:
        List_of_ratings_total.append(get_rating_movie_user(ratings,user_id,movie))

    #Making sure everything is an integer
    length2 = len(List_of_ratings_total)
    i=0
    while i< length2 -1:
        List_of_ratings_total[i]= int(List_of_ratings_total[i])
        i=i+1


    if length !=0:
        average_rating_recommended = sum(List_of_ratings)/length #The average rating the user gave to the movies that are recommended to him and he watched in the past
    average_rating_total =sum(List_of_ratings_total)/length2 # The average rating this user gave to all of the movies
    recommended_average.append((average_rating_recommended))
    rated_average.append(average_rating_total)
    

print("recommended average :" + str((sum(recommended_average)/len(recommended_average))))
print("rated average :" + str((sum(rated_average)/len(rated_average))))

##We display the average ratings of recommended movies for each user and the average rating given by users so we can compare the two and see if people actually like the movies that are recommended to them
##Better to be run with a smaller amount of users due to the power needed to go through the whole dataset, the algorithm is not necesseraly optimised