from flask import Flask, render_template, request, redirect

app = Flask(__name__)

movies = [
    {"name": "The Dark Knight", "rating": 90},
    {"name": "Star Wars", "rating": 86},
    {"name": "Casablanca", "rating": 82},
    {"name": "Memento", "rating": 79},
    {"name": "Toy Story", "rating": 75},
    {"name": "Die Hard", "rating": 68}
]


@app.route('/')
def home():
    return render_template("index.html", movies=movies)

# Hello world!

@app.route('/info')
def info():
    # ?movie=2
    movie_index = int(request.args["movie"])
    return render_template("info.html",
                           name=movies[movie_index]["name"],
                           rating=movies[movie_index]["rating"])


@app.route('/remove/<int:movie>', methods=["GET"])
def remove(movie):
    movies.pop(movie)
    return redirect('/')


@app.route('/add', methods=["POST"])
def add():
    movie_name = request.form["name"]
    movie_rating = int(request.form["rating"])
    new_movie = {"name": movie_name, "rating": movie_rating}
    movies.append(new_movie)
    return redirect('/')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
