import pandas as pd
import numpy as np
import zipfile
import pathlib


def get_ratings_matrix():
    dir_ref = pathlib.Path('the-movies-dataset')
    if not (dir_ref.is_dir() and dir_ref.exists()):
        zip_ref = zipfile.ZipFile('the-movies-dataset.zip', 'r')
        zip_ref.extractall('./')
    movies_dataset = pd.read_csv('./the-movies-dataset/ratings_small.csv')
    ratings = movies_dataset.values
    movie_ids = np.array(movies_dataset.iloc[:, 1].unique())
    no_movie_ids = movie_ids.max() + 1
    user_ids = np.array(movies_dataset.iloc[:, 0].unique())
    no_user_ids = user_ids.max()
    matrix = np.zeros((no_user_ids, no_movie_ids))
    for i in range(1, no_user_ids + 1):
        var1 = (ratings[ratings[:, 0] == i])[:, 1]
        var1 = var1.astype(int)
        var2 = (ratings[ratings[:, 0] == i])[:, 2]
        temp = np.zeros(no_movie_ids)
        temp[var1] = var2
        matrix[i - 1] = temp
    matrix = matrix.transpose()
    temp = np.arange(1, matrix.shape[0] + 1).reshape(matrix.shape[0], 1)
    matrix = np.hstack([temp, matrix])
    user_ids = np.insert(user_ids, 0, 0)
    matrix = np.vstack([user_ids, matrix])
    ratings = pd.DataFrame(data=matrix[1:, 1:], index=matrix[1:, 0], columns=matrix[0, 1:])
    ratings.index = ratings.index.astype('int32')
    ratings.columns = ratings.columns.astype('int32')
    ratings.index.name = "id"
    return ratings


ratings = get_ratings_matrix()
