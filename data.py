import pandas as pd
from functions import Scaling_dataset
users = pd.read_csv("data/users.csv")
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

genre_cols = ["Animation", "Children's",
       'Comedy', 'Adventure', 'Fantasy', 'Romance', 'Drama',
       'Action', 'Crime', 'Thriller', 'Horror', 'Sci-Fi', 'Documentary', 'War',
       'Musical', 'Mystery', 'Film-Noir', 'Western']



##Scaling each column of the dataset in case a new one is added and it does not follow the same format
movies = Scaling_dataset(movies)

