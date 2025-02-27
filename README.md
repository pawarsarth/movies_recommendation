# movies_recommendation

# 🎬 Movie Recommendation System (Flask + ML)  

A **Flask-based Movie Recommendation System** that suggests similar movies based on user ratings. This project uses **Machine Learning (Cosine Similarity)** to analyze movie ratings and provide personalized recommendations.  

---

## 🚀 Features  

✅ **Custom Movie Dataset** – Uses a dataset of movies and user ratings.  
✅ **Data Processing** – Merges `movies.csv` and `ratings.csv` to create a **User-Movie rating matrix**.  
✅ **Machine Learning** – Computes **cosine similarity** between movies to find similar ones.  
✅ **Flask API** – Accepts user movie preferences and returns **real-time recommendations**.  
✅ **Dynamic Suggestions** – Generates recommendations on the fly without precomputed data.  

---

## 🛠 Tech Stack  

🔹 **Python** – Data processing & ML calculations  
🔹 **Pandas** – Dataset merging & pivot tables  
🔹 **Scikit-Learn** – Cosine similarity calculations  
🔹 **Flask** – API development  
🔹 **Postman** – Testing API requests  

---

## 📂 Dataset  

This project uses **two datasets**:  

1️⃣ **movies.csv** – Contains movie titles and genres  
2️⃣ **ratings.csv** – Contains user ratings for movies  

Example:  

**movies.csv**  
```csv
movieId,title,genres
1,Inception (2010),Sci-Fi
2,Titanic (1997),Romance
3,The Dark Knight (2008),Action
```

**ratings.csv**  
```csv
userId,movieId,rating,timestamp
101,1,5.0,1620000000
101,3,4.5,1620000100
102,2,4.0,1620000200
```

---

## 📌 How It Works  

1️⃣ **Load & merge datasets** (movies + ratings)  
2️⃣ **Create a user-movie rating matrix**  
3️⃣ **Compute similarity scores** using **cosine similarity**  
4️⃣ **Build a Flask API** that takes user input (favorite movies & ratings)  
5️⃣ **Return top recommended movies** based on similarity scores  

---

## 🔧 Installation & Setup  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/yourusername/movie-recommendation-flask.git
cd movie-recommendation-flask
```

2️⃣ **Install dependencies**  
```bash
pip install flask pandas scikit-learn
```

3️⃣ **Run the Flask app**  
```bash
python app.py
```

4️⃣ **Send a POST request to `/recommend`** with your favorite movies & ratings  
Example:  
```json
{
    "movies": [
        ["Inception (2010)", 5],
        ["Titanic (1997)", 4]
    ]
}
```

5️⃣ **Get movie recommendations in response! 🎥**  

---

## 🎯 Future Improvements  

🔹 Add a **frontend UI** for easy interaction  
🔹 Expand the **movie dataset** for better recommendations  
🔹 Implement **collaborative filtering** for user-based recommendations  

---

## 🤝 Contributing  

Feel free to **fork** this repo and submit **pull requests**. Contributions are always welcome! 🚀  

---
