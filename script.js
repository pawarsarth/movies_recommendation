let selectedMovies = [];

function addMovie() {
    let movieName = document.getElementById("movie-name").value;
    let movieRating = document.getElementById("movie-rating").value;

    if (movieName && movieRating) {
        selectedMovies.push([movieName, parseInt(movieRating)]);
        document.getElementById("movie-list").innerHTML += `<li>${movieName} (⭐ ${movieRating})</li>`;
        document.getElementById("movie-name").value = "";
        document.getElementById("movie-rating").value = "";
    } else {
        alert("Please enter both movie name and rating.");
    }
}

function getRecommendations() {
    fetch('/recommend', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ movies: selectedMovies })
    })
    .then(response => response.json())
    .then(data => {
        let resultDiv = document.getElementById("results");
        resultDiv.innerHTML = "<h2>Recommended Movies</h2>";
        
        for (let movie in data) {
            if (data[movie].error) {
                resultDiv.innerHTML += `<p>${data[movie].error}</p>`;
            } else {
                resultDiv.innerHTML += `<h3>${movie} Recommendations:</h3><ul>`;
                for (let rec in data[movie]) {
                    resultDiv.innerHTML += `<li>${rec} (Score: ${data[movie][rec].toFixed(2)})</li>`;
                }
                resultDiv.innerHTML += "</ul>";
            }
        }
    });
}
