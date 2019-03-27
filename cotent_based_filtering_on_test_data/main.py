from cotent_based_filtering_on_test_data.filter import filter
import numpy as np
from sklearn.linear_model import LinearRegression

X, ratings_vector, movies_ids, user_ids, list_genres, movie_names = filter()
clf = LinearRegression()
top_5_recommendations = np.empty((ratings_vector.shape[1], 5),dtype=np.dtype(object))
for i in range(ratings_vector.shape[1]):
    single_y = ratings_vector[:, i]
    if single_y[single_y != 0].shape[0] != 0:
        positions = np.nonzero(single_y)[0]
        remaining_positions = np.where(single_y == 0)[0]
        reg = clf.fit(X[positions], single_y[positions])
        predictions = reg.predict(X[remaining_positions])
        top_5_recommendations_each = movies_ids[np.argsort(predictions)[-5:]]
        top_5_recommendations[i] = movie_names.loc[top_5_recommendations_each,:].values.reshape(1,5)[0]

print(top_5_recommendations)
