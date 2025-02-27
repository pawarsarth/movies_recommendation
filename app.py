from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Step 1: Load Custom Dataset
movies = pd.read_csv("movies1.csv")  # Movie information
ratings = pd.read_csv("rating1.csv")  # User ratings

# Step 2: Merge datasets on 'movieId'
merged_data = pd.merge(ratings, movies, on="movieId").drop(["genres", "timestamp"], axis=1)

# Step 3: Create User-Movie Rating Matrix
user_movie_ratings = merged_data.pivot_table(index="userId", columns="title", values="rating")

# Step 4: Compute Item Similarity Matrix
item_similarity_df = pd.DataFrame(
    cosine_similarity(user_movie_ratings.fillna(0).T),  # Transpose for movie similarity
    index=user_movie_ratings.columns,
    columns=user_movie_ratings.columns
)

def get_similar_movies(movie_name, user_rating):
    """Fetch similar movies based on user input rating."""
    if movie_name not in item_similarity_df.columns:
        return {"error": f"'{movie_name}' not found in dataset."}

    # Compute similarity scores
    similar_score = item_similarity_df[movie_name] * (user_rating - 2.5)
    similar_score = similar_score.sort_values(ascending=False).head(5)

    return similar_score.to_dict()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_movies = data.get('movies', [])

    recommendations = {}
    for movie, rating in user_movies:
        result = get_similar_movies(movie, rating)
        recommendations[movie] = result

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
