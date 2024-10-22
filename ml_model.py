import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import pickle
import threading

# Global variable to store the model
model = None

# Load MovieLens dataset
def load_data():
    file_path = 'ml-100k/u.data'
    reader = Reader(line_format='user item rating timestamp', sep='\t')
    df = pd.read_csv(file_path, sep='\t', names=['userID', 'itemID', 'rating', 'timestamp'])
    data = Dataset.load_from_df(df[['userID', 'itemID', 'rating']], reader)
    return df, data

# Train the model (in the background)
def train_model_in_background():
    global model
    df, data = load_data()
    trainset, testset = train_test_split(data, test_size=0.25)
    algo = SVD()
    algo.fit(trainset)
    model = algo

    # Save the model after training
    with open('svd_model.pkl', 'wb') as f:
        pickle.dump(algo, f)

# Load the trained model from disk
def load_model():
    global model
    with open('svd_model.pkl', 'rb') as f:
        model = pickle.load(f)

# Generate movie recommendations using the trained model
def get_recommendations(user_id, num_recommendations=5):
    global model
    if model is None:
        load_model()

    # Load movie data for titles
    movie_file = 'ml-100k/u.item'
    movies_df = pd.read_csv(movie_file, sep='|', encoding='latin-1', header=None, usecols=[0, 1], names=['movieID', 'title'])

    # Get a list of all movie IDs
    all_movie_ids = movies_df['movieID'].unique()

    # Predict ratings for movies the user hasn't rated
    predicted_ratings = [(movie, model.predict(user_id, movie).est) for movie in all_movie_ids]

    # Sort by predicted rating and get the top recommendations
    recommended_movies = sorted(predicted_ratings, key=lambda x: x[1], reverse=True)[:num_recommendations]
    recommended_movie_ids = [movie[0] for movie in recommended_movies]
    recommended_movie_titles = movies_df[movies_df['movieID'].isin(recommended_movie_ids)]['title'].tolist()

    return recommended_movie_titles

# Start the background thread for model training
def start_background_training():
    thread = threading.Thread(target=train_model_in_background)
    thread.start()
