from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
movies = []
bookings = []

# GET all movies
@app.route('/api/movies', methods=['GET'])
def get_movies():
    return jsonify(movies), 200

# GET movie by ID
@app.route('/api/movies/<int:id>', methods=['GET'])
def get_movie(id):
    movie = next((m for m in movies if m["id"] == id), None)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404
    return jsonify(movie), 200

# POST add new movie
@app.route('/api/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    if not data or "id" not in data:
        return jsonify({"error": "Invalid data"}), 400
    movies.append(data)
    return jsonify(data), 201

# PUT update movie
@app.route('/api/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    movie = next((m for m in movies if m["id"] == id), None)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404
    data = request.get_json()
    movie.update(data)
    return jsonify(movie), 200

# DELETE movie
@app.route('/api/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    global movies
    movies = [m for m in movies if m["id"] != id]
    return jsonify({"message": "Deleted"}), 200

# POST booking
@app.route('/api/bookings', methods=['POST'])
def book_ticket():
    data = request.get_json()
    if not data or "movie_id" not in data:
        return jsonify({"error": "Invalid booking"}), 400
    movie = next((m for m in movies if m["id"] == data["movie_id"]), None)
    if not movie:
        return jsonify({"error": "Movie not found"}), 404
    bookings.append(data)
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)
