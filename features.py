import pandas as pd
import numpy as np
import zipfile
import pathlib
import json

# global variable
set_genres = set()
dict_genres = {}


def get_genres(x):
    js = json.loads(str(x))
    genres = [li['name'] for li in js]
    set(genres)
    return genres


def list_genres(x):
    global set_genres
    set_genres |= set(x)


def features(x):
    global dict_genres
    list_feature = [0] * len(dict_genres)
    if len(x) == 0:
        return np.nan
    value = 1.0 / (float(len(x)))
    for item in x:
        list_feature[dict_genres[item]] = value
    return np.around(list_feature, decimals=2)


features_matrix = np.arange(20).reshape((1, 20))


def generate_features_matrix(x):
    global features_matrix
    x.reshape((1, 20))
    features_matrix = np.vstack([features_matrix, x])


def get_features():
    dir_ref = pathlib.Path('the-movies-dataset')
    if not (dir_ref.is_dir() and dir_ref.exists()):
        zip_ref = zipfile.ZipFile('the-movies-dataset.zip', 'r')
        zip_ref.extractall('./')
    movies_metadata = pd.read_csv('./the-movies-dataset/movies_metadata.csv', low_memory=False)
    movies_metadata.drop(movies_metadata[movies_metadata.id == "1997-08-20"].index, inplace=True)
    movies_metadata.drop(movies_metadata[movies_metadata.id == "2012-09-29"].index, inplace=True)
    movies_metadata.drop(movies_metadata[movies_metadata.id == "2014-01-01"].index, inplace=True)
    movies_metadata["genres"] = movies_metadata.genres.apply(lambda x: str(x).replace("'", '"'))
    movies_metadata["belongs_to_collection"] = movies_metadata.belongs_to_collection.apply(
        lambda x: str(x).replace("'", '"'))
    movies_metadata["genres_list"] = movies_metadata.genres.apply(get_genres)
    movies_metadata.genres_list.apply(list_genres)
    global set_genres
    global dict_genres
    set_genres = list(set_genres)
    set_genres.sort()
    for index, item in enumerate(set_genres):
        dict_genres[item] = index
    movies_metadata["features_genres"] = movies_metadata["genres_list"].apply(features)
    movies_metadata.dropna(subset=['features_genres'], inplace=True)
    features_dataframe = movies_metadata.loc[:, ['id', 'features_genres']]
    features_dataframe.set_index(['id'], inplace=True)
    movie_ids = movies_metadata['id'].values
    movie_ids = movie_ids.astype(np.int)
    features_dataframe.features_genres.apply(generate_features_matrix)
    features_dataframe = pd.DataFrame(data=features_matrix[1:, :], columns=features_matrix[0, :], index=movie_ids)
    features_dataframe.index.name = 'id'
    features_dataframe.columns = features_dataframe.columns.astype('int32')
    features_dataframe.index = features_dataframe.index.astype('int32')
    return features_dataframe, movie_ids, np.array(list(set_genres))
