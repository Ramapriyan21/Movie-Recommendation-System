import requests

API_KEY = '642a00b58f9056ff281821708e7162fc'

# Fetch movies from TMDb based on genre and rating
def get_tmdb_movies(genre, min_rating):
    genre_map = {
        'action': 28,
        'comedy': 35,
        'drama': 18,
        'sci-fi': 878,
        'romance': 10749
    }
    
    genre_id = genre_map.get(genre)
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}&vote_average.gte={min_rating}&sort_by=popularity.desc'
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    else:
        return []
