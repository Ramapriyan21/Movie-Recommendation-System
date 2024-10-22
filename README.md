# Personalized Movie Recommendation System

This project is a simple **movie recommendation system** using **collaborative filtering** (with **SVD**) and **content-based filtering** (using the **TMDb API**). It allows users to get movie recommendations based on their **genre preference** and **previous movie ratings**.

## Features
- Users select a **genre** and specify a **minimum rating**.
- Users input their **user ID** to receive personalized recommendations based on past ratings.
- The system fetches popular movies from **TMDb** and also provides personalized recommendations using **collaborative filtering**.
  
## Technologies Used
- **Python**: Backend logic and model training
- **Flask**: Web framework for serving the application
- **TMDb API**: For fetching movie data
- **Surprise**: Machine learning library for collaborative filtering (SVD model)
- **HTML/CSS**: For the front-end interface

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/movie-recommendation-app.git
cd movie-recommendation-app

