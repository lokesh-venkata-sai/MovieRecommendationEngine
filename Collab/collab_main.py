import numpy as np
from scipy.optimize import minimize


def cost_function(grad):
    global movie_features_X, user_features_theta,no_of_movies,no_of_users
    grad = grad.reshape(no_of_movies + no_of_users, no_of_features)
    movie_features_X = grad[:no_of_movies, :]
    user_features_theta = grad[no_of_movies:, :]
    theta_times_x = movie_features_X.dot(user_features_theta.transpose()) % 5
    return np.sum(((theta_times_x - ratings) ** 2) / 2)


def grad_function(grad):
    global movie_features_X, user_features_theta, no_of_movies, no_of_users
    grad = grad.reshape(no_of_movies + no_of_users, no_of_features)
    movie_features_X = grad[:no_of_movies, :]
    user_features_theta = grad[no_of_movies:, :]
    theta_times_x = movie_features_X.dot(user_features_theta.transpose()) % 5
    grad_X = (theta_times_x - ratings).dot(user_features_theta)
    grad_theta = ((theta_times_x - ratings).transpose()).dot(movie_features_X)
    return np.vstack((grad_X, grad_theta)).flatten()


no_of_movies = 50
no_of_users = 50
no_of_features = 30
ratings = np.around(5 * np.random.rand(no_of_movies, no_of_users))
movie_features_X = np.random.rand(no_of_movies, no_of_features)
user_features_theta = np.random.rand(no_of_users, no_of_features)
X0 = np.vstack((movie_features_X, user_features_theta))
X0 = X0.flatten()
sol = minimize(fun=cost_function, x0=X0, method="BFGS", jac=grad_function, options={'maxiter': 500})
