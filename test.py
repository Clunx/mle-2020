##This is the testing program

from data import ratings, movies, genre_cols  #importing all the data, everything can be changed there when changing datasets
from functions import get_most_similar,get_recommendations



test_user_id = int(input("user id: "))

if type(test_user_id) != int:
    print("Not an integer")
else:
    #genre_and_title_cols = ['title'] + genre_cols cette ligne n'est pas nécéscairre
    similarity_mat = movies[genre_cols].values.dot(movies[genre_cols].values.T)

    print(get_recommendations(test_user_id,ratings,similarity_mat,movies))
