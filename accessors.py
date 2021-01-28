
def get_user_id(users, index):
    return users.iloc[index].id
def get_user_gender(users, index):
    return users.iloc[index].gender
def get_user_age(users, index):
    return users.iloc[index].age
def get_user_occupation(users, index):
    return users.iloc[index].occupation
def get_user_zipcode(users, index):
    return users.iloc[index].zipcode

def get_ratings_user(ratings,user_id):
    user_movies = ratings[ratings['user_id'] == user_id]
    return user_movies.iloc[:,1:]
def get_rating_movie_user(ratings,user_id,movie_id):
    user_movies = ratings[ratings['user_id'] == user_id]
    user_movie= user_movies[user_movies['movie_id']== movie_id]
    rating = user_movie.iloc[0]['rating']
    return rating