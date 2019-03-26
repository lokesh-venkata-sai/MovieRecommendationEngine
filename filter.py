from features import get_features
from Ratings_matrix import get_ratings_matrix


def filter():
    ratings, movie_ids_ratings, user_ids = get_ratings_matrix()
    features_dataframe, movie_ids_features, list_genres = get_features()
    movie_ids_ratings = set(movie_ids_ratings)
    movie_ids_features = set(movie_ids_features)
    movies_common = movie_ids_features.intersection(movie_ids_ratings)
    movies_common = list(movies_common)
    ratings = ratings.loc[movies_common, :]
    features_dataframe = features_dataframe.loc[movies_common, :]
    return features_dataframe.values[1:, :], ratings.values[:, 1:], movies_common, user_ids, list_genres


feature_vector, ratings_vector, movies_ids, user_ids, list_genres = filter()
print(feature_vector)
print("The above matrix are 20 different genres features for 2800 movies")
print()
print("the feature vector representation of movieId " + str(movies_ids[0]))
print(feature_vector[0])
print()
print(list_genres)
print("These are the genres considered for each movie")


print()
print()
print()
print()


print(ratings_vector)
print("The above matrix are ratings given by 671 users for 2800 movies")
print()
print("these are ratings given by 671 users for movieId " + str(movies_ids[0]))
print(ratings_vector[0])