from flask import Flask, render_template, request
from ml_model import start_background_training, get_recommendations
from tmdb_fetcher import get_tmdb_movies

app = Flask(__name__, static_url_path='/static')  # Explicitly set the static URL path

# Start background model training when the app starts
start_background_training()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user inputs for genre, rating, and user_id
        genre = request.form.get('genre')
        rating = request.form.get('rating')
        user_id = request.form.get('user_id')

        # Fetch movies from TMDb based on genre and minimum rating
        tmdb_movies = get_tmdb_movies(genre, float(rating))

        # Get personalized recommendations using collaborative filtering model (SVD)
        model_recommendations = get_recommendations(int(user_id))

        # Render the recommendations page
        return render_template('recommendations.html', tmdb_movies=tmdb_movies, model_recommendations=model_recommendations)

    # Render the index page for user input
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
