import pandas as pd
from content_based_filtering.helpers.movies import get_movie_id, get_movie_name, get_movie_year

def get_most_similar(similarity, movie_name,movies, year=None, top=10):
    index_movie = get_movie_id(movies, movie_name, year)
    best = similarity[index_movie].argsort()[::-1]
    return [(ind, get_movie_name(movies, ind), similarity[index_movie, ind]) for ind in best[:top] if ind != index_movie]



def get_recommendations(user_id,ratings,similarity,movies):
    top_movies = ratings[ratings['user_id'] == user_id].sort_values(by='rating', ascending=False).head(6)['movie_id']
    index=['movie_id', 'title', 'similarity']

    most_similars = []

    for top_movie in top_movies:

        most_similars += get_most_similar(similarity, get_movie_name(movies, top_movie),movies, get_movie_year(movies, top_movie))

    return pd.DataFrame(most_similars, columns=index).drop_duplicates().sort_values(by='similarity', ascending=False).head(5)


def Scaling_dataset(D):
    D_scaled = D
    D_left = D.iloc[:, :3]
    D_scaled = D.iloc[:, 3:]

    # apply maximum absolute scaling
    for column in D_scaled.columns:
        D_scaled[column] = D_scaled[column] - D_scaled[column].min()
        D_scaled[column] = D_scaled[column] / D_scaled[column].max()

    D_scaled.reset_index(drop=True, inplace=True)
    D_left.reset_index(drop=True, inplace=True)
    D_scaled = pd.concat([D_left, D_scaled], axis=1)

    return D_scaled
