import requests
import pytest

BASE_URL = "http://127.0.0.1:5000/api/v1"

class TestFoodieApp:
    # Class-level variables to store IDs dynamically
    rest_id = None
    dish_id = None
    user_id = None
    order_id = None

    # --- RESTAURANT MODULE ---

    def test_register_restaurant(self):
        """Req #1: Register Restaurant"""
        payload = {
            "name": "Pytest Delight",
            "location": "Hyderabad",
            "category": "Main Course",
            "contact": "9876543210"
        }
        response = requests.post(f"{BASE_URL}/restaurants", json=payload)
        assert response.status_code == 201
        TestFoodieApp.rest_id = response.json()["id"]
        assert response.json()["name"] == "Pytest Delight"

    def test_register_restaurant_conflict(self):
        """Req #1: Conflict Check"""
        payload = {"name": "Pytest Delight", "location": "Hyderabad"}
        response = requests.post(f"{BASE_URL}/restaurants", json=payload)
        assert response.status_code == 409

    def test_update_restaurant(self):
        """Req #2: Update Restaurant"""
        payload = {"location": "Vijayawada"}
        response = requests.put(f"{BASE_URL}/restaurants/{self.rest_id}", json=payload)
        assert response.status_code == 200
        assert response.json()["location"] == "Vijayawada"

    def test_disable_restaurant(self):
        """Req #3: Disable Restaurant"""
        response = requests.put(f"{BASE_URL}/restaurants/{self.rest_id}/disable")
        assert response.status_code == 200

    def test_get_restaurant_profile(self):
        """Req #4: Get Profile"""
        response = requests.get(f"{BASE_URL}/restaurants/{self.rest_id}")
        assert response.status_code == 200

    # --- DISH MODULE ---

    def test_add_dish(self):
        """Req #5: Add Dish"""
        payload = {"name": "Biryani", "type": "Non-Veg", "price": 250}
        response = requests.post(f"{BASE_URL}/restaurants/{self.rest_id}/dishes", json=payload)
        assert response.status_code == 201
        TestFoodieApp.dish_id = response.json()["id"]

    def test_update_dish(self):
        """Req #6: Update Dish"""
        payload = {"price": 300}
        response = requests.put(f"{BASE_URL}/dishes/{self.dish_id}", json=payload)
        assert response.status_code == 200
        assert response.json()["price"] == 300

    def test_toggle_dish(self):
        """Req #7: Toggle Status"""
        payload = {"enabled": False}
        response = requests.put(f"{BASE_URL}/dishes/{self.dish_id}/status", json=payload)
        assert response.status_code == 200

    def test_delete_dish(self):
        """Req #8: Delete Dish"""
        response = requests.delete(f"{BASE_URL}/dishes/{self.dish_id}")
        assert response.status_code == 200

    # --- USER & ORDER MODULE ---

    def test_register_user(self):
        """Req #13: Register User"""
        payload = {"name": "Alice", "email": "alice_pytest@test.com"}
        response = requests.post(f"{BASE_URL}/users/register", json=payload)
        assert response.status_code == 201
        TestFoodieApp.user_id = response.json()["id"]

    def test_search_restaurant(self):
        """Req #14: Search Restaurant"""
        params = {"name": "Pytest", "location": "Vijayawada"}
        response = requests.get(f"{BASE_URL}/restaurants/search", params=params)
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_place_order(self):
        """Req #15: Place Order"""
        # Note: We use a static dish_id 1 if the previous delete test was run,
        # or recreate a dish if necessary.
        payload = {
            "user_id": self.user_id,
            "restaurant_id": self.rest_id,
            "items": [{"dish_id": 1, "qty": 2}]
        }
        response = requests.post(f"{BASE_URL}/orders", json=payload)
        assert response.status_code == 201
        TestFoodieApp.order_id = response.json()["id"]

    def test_give_rating(self):
        """Req #16: Give Rating"""
        payload = {"order_id": self.order_id, "rating": 5, "comment": "Great!"}
        response = requests.post(f"{BASE_URL}/ratings", json=payload)
        assert response.status_code == 201

    # --- ADMIN MODULE ---

    def test_admin_approve(self):
        """Req #9: Admin Approve"""
        response = requests.put(f"{BASE_URL}/admin/restaurants/{self.rest_id}/approve")
        assert response.status_code == 200

    def test_admin_view_feedback(self):
        """Req #11: View Feedback"""
        response = requests.get(f"{BASE_URL}/admin/feedback")
        assert response.status_code == 200

    def test_admin_view_orders(self):
        """Req #12: View All Orders"""
        response = requests.get(f"{BASE_URL}/admin/orders")
        assert response.status_code == 200