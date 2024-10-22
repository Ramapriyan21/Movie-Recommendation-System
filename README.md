# Personalized Movie Recommendation System

This project is a simple movie recommendation system using collaborative filtering (with SVD) and content-based filtering (using the TMDb API). It allows users to get movie recommendations based on their genre preference and previous movie ratings.

## Features

- **Genre Selection**: Users can select a genre and specify a minimum rating.
- **User ID Input**: Users input their user ID to receive personalized recommendations based on past ratings.
- **TMDb Data**: Fetches popular movies from TMDb based on genre and rating.
- **Collaborative Filtering**: Provides personalized movie recommendations using collaborative filtering (SVD model).
  
## Requirements

To run this project, you need Python and the following libraries:

- Python 3.x
- `Flask`
- `Surprise` (for collaborative filtering)
- `pandas`
- `requests`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/movie-recommendation-app.git
    cd movie-recommendation-app
    ```

2. Install the necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the MovieLens 100k dataset from [here](https://grouplens.org/datasets/movielens/100k/) and place the `u.data` and `u.item` files in a folder named `ml-100k` inside the project directory.

4. Get a TMDb API key by signing up at [TMDb](https://www.themoviedb.org/) and add it to the `tmdb_fetcher.py` file:
    ```python
    API_KEY = 'your_tmdb_api_key'
    ```

## How to Run

1. Start the Flask application:
    ```bash
    python app.py
    ```

2. Open your browser and go to `http://127.0.0.1:5000/`.

3. Select a genre, specify a minimum rating, and enter your user ID to get personalized movie recommendations.

## Available Features

- **Genre Selection**: Choose from popular genres such as Action, Comedy, Drama, etc.
- **Personalized Recommendations**: Based on your previous movie ratings, the app suggests movies using collaborative filtering (SVD).
- **TMDb API**: Fetches movie details such as title, rating, and overview from the TMDb database based on the genre and rating.
  
## Customization

You can expand the recommendation system by adding more genres or integrating with other movie databases. You can also implement additional filtering options like runtime or actors.

## Known Issues

- Make sure the `u.data` and `u.item` files from MovieLens 100k are placed in the `ml-100k` folder.
- The app relies on an internet connection for fetching TMDb data.

## License

This project is open-source. Feel free to modify and use it as needed.
