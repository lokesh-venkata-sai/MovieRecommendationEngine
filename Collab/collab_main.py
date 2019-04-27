import numpy as np
import pandas as pd
from scipy.optimize import minimize
import pymysql
from pandas.io import sql as s
from sqlalchemy import create_engine

def cost_function(grad):
    global ratings, no_of_features, no_of_movies, no_of_users
    grad = grad.reshape(no_of_movies + no_of_users, no_of_features)
    movie_features_X = grad[:no_of_movies, :]
    user_features_theta = grad[no_of_movies:, :]
    theta_times_x = movie_features_X.dot(user_features_theta.transpose())
    R = np.ones(ratings.shape)
    R[ratings == 0] = 0
    theta_times_x = theta_times_x * R
    ratings_temp = ratings * R
    return np.sum(((theta_times_x - ratings_temp) ** 2) / 2)


def grad_function(grad):
    global ratings, no_of_features, no_of_movies, no_of_users
    grad = grad.reshape(no_of_movies + no_of_users, no_of_features)
    movie_features_X = grad[:no_of_movies, :]
    user_features_theta = grad[no_of_movies:, :]
    theta_times_x = movie_features_X.dot(user_features_theta.transpose())
    R = np.ones(ratings.shape)
    R[ratings == 0] = 0
    theta_times_x = theta_times_x * R
    ratings_temp = ratings * R
    grad_X = (theta_times_x - ratings_temp).dot(user_features_theta)
    grad_theta = ((theta_times_x - ratings_temp).transpose()).dot(movie_features_X)
    return np.vstack((grad_X, grad_theta)).flatten()


def get_matrix(csv_file):
    movies_dataset = pd.read_csv(csv_file, low_memory=False)
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
    matrix = np.delete(matrix, 0, 0)
    return matrix


def recommendations():
    global no_of_users, no_of_movies, no_of_features, ratings
    ratings = get_matrix('ratings_filtered_510.csv')
    no_of_users = ratings.shape[1]
    no_of_movies = ratings.shape[0]
    no_of_features = 15
    movie_features_X = np.random.rand(no_of_movies, no_of_features)
    user_features_theta = np.random.rand(no_of_users, no_of_features)
    grad = np.vstack((movie_features_X, user_features_theta))
    grad = grad.flatten()
    sol = minimize(fun=cost_function, x0=grad, method="BFGS", jac=grad_function, options={'maxiter': 50})
    solution = sol.x.reshape(no_of_movies + no_of_users, no_of_features)
    solution_movie_features = solution[:no_of_movies, :]
    solution_user_theta = solution[no_of_movies:, :]
    ratings_predicted = solution_movie_features.dot(solution_user_theta.transpose())
    R = np.zeros(ratings.shape)
    R[ratings == 0] = 1
    ratings_predicted = ratings_predicted * R
    predictions = pd.DataFrame(data=ratings_predicted, columns=np.arange(1, no_of_users + 1),
                               index=np.arange(1, no_of_movies + 1))
    top_5_predictions = pd.DataFrame(columns=['userId', 'movieId'])
    for i in range(1, no_of_users + 1):
        for_each_user = predictions.nlargest(6, [i]).loc[:, [i]]
        for_each_user['userId'] = np.full(6, i)
        for_each_user['movieId'] = for_each_user.index
        for_each_user.index = np.arange(6)
        top_5_predictions = top_5_predictions.append(for_each_user.loc[:, ['userId', 'movieId']], ignore_index=True)
    return top_5_predictions




if __name__ == "__main__":
    x = recommendations()
    cnx = create_engine('mysql+pymysql://root:lokesh1999@localhost:3306/movieRecommendation').connect()
    x.to_sql(con=cnx,name='recommend',if_exists='replace',dtype=None,index=True)
    print("done")