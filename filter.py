import features
import Ratings_matrix


def filter():
    ratings, movie_ids_ratings, user_ids = Ratings_matrix.get_ratings_matrix()
    features_dataframe, movie_ids_features, list_genres = features.get_features()
    movie_ids_ratings = set(movie_ids_ratings)
    movie_ids_features = set(movie_ids_features)
    movies_common = movie_ids_features.intersection(movie_ids_ratings)
    ratings = ratings.loc[list(movies_common), :]
    # features_dataframe = features_dataframe.loc[list(movies_common), :]
    return features_dataframe, ratings, movies_common, user_ids


features_dataframe, ratings, movies_common, user_ids = filter()
print(features_dataframe.head())
