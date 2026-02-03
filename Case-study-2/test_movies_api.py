import requests

BASE = "http://127.0.0.1:5000"

def test_get_movies_initial():
    r = requests.get(f"{BASE}/api/movies")
    assert r.status_code == 200

def test_add_movie():
    payload = {
        "id": 401,
        "movie_name": "Inception",
        "language": "English",
        "duration": "2h 28m",
        "price": 300
    }
    r = requests.post(f"{BASE}/api/movies", json=payload)
    assert r.status_code == 201

def test_get_movie_by_id():
    r = requests.get(f"{BASE}/api/movies/401")
    assert r.status_code == 200
    assert r.json()["movie_name"] == "Inception"

def test_update_movie():
    r = requests.put(f"{BASE}/api/movies/401", json={"price":350})
    assert r.status_code == 202 or r.status_code == 200

def test_delete_movie():
    r = requests.delete(f"{BASE}/api/movies/401")
    assert r.status_code == 200

def test_book_ticket_success():
    movie = {"id":501, "movie_name":"Avatar","language":"English","duration":"2h 40m","price":200}
    requests.post(f"{BASE}/api/movies", json=movie)
    booking = {"movie_id":501, "user":"Alice", "seats":2}
    r = requests.post(f"{BASE}/api/bookings", json=booking)
    assert r.status_code == 201

def test_book_ticket_fail():
    r = requests.post(f"{BASE}/api/bookings", json={"movie_id":999})
    assert r.status_code == 404
