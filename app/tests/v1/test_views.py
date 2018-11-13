import pytest
import json
from app import create_app


@pytest.fixture
def my_app():
    """"Method to initialize app and test_client."""
    app = create_app()
    test_client = app.test_client()
    return test_client
orders = {"order_id": 101, "user_id": 1, "pickup_location": "Nairobi",
          "destination": "Kisumu", "weight": 20, "quote": 2000, "status": "in transit"}
users = {"user_id": 201, "username": "Rachel", "password": "root",
         "phone": 712345123, "email": "rachel@gmail.com"}


class TestOrderViews(object):
    """"Class to test Order delivery views."""

    def test_get_all_orders(self, my_app):
        """"Method to test if all parcel order deliveries are fetched."""
        res = my_app.get("/api/v1/parcels")

        res_data = json.loads(res.data.decode())
        assert res.status_code == 200
        assert "Ok" in res_data["status"]

    def test_get_one_order(self, my_app):
        """"Method to test if one parcel order delivery are fetched."""
        res = my_app.get("/api/v1/parcels/101")

        res_data = json.loads(res.data.decode())
        assert res.status_code == 200
        assert "Ok" in res_data["status"]

    def test_get_all_orders_by_user(self, my_app):
        """"Method to test if all parcel order deliveries are by a specific user are fetched."""
        res = my_app.get("/api/v1/users/1/parcels")

        res_data = json.loads(res.data.decode())
        assert res.status_code == 200
        assert "Ok" in res_data["status"]

    def test_create_order(self, my_app):
        """"Method to test if a parcel order delivery is created."""
        res = my_app.post("api/v1/parcels", data=json.dumps(orders),
                          content_type="application/json;charset=utf-8")

        res_data = json.loads(res.data.decode())
        assert res.status_code == 201
        assert "Created" in res_data["status"]

    def test_cancel_order(self, my_app):
        """"Method to test if a parcel delivery order is cancelled."""
        res = my_app.put("api/v1/parcels/101/cancel", data=json.dumps(orders),
                         content_type="application/json;charset=utf-8")

        res_data = json.loads(res.data.decode())
        assert res.status_code == 200
        assert "Order Cancelled" in res_data["Status"]


class TestUserViews(object):
    """"Class to test Order delivery views."""

    def test_get_all_users(self, my_app):
        """"Method to test if all users are fetched."""
        res = my_app.get("/api/v1/users")

        res_data = json.loads(res.data.decode())
        assert res.status_code == 200
        assert "Ok" in res_data["status"]

    def test_get_one_user(self, my_app):
        """"Method to test if one user fetched."""
        res = my_app.get("/api/v1/users/201")

        res_data = json.loads(res.data.decode())
        assert res.status_code == 200
        assert "Ok" in res_data["status"]

    def test_create_user(self, my_app):
        """"Method to test if a user is created."""
        res = my_app.post("api/v1/users", data=json.dumps(users),
                          content_type="application/json;charset=utf-8")

        res_data = json.loads(res.data.decode())
        assert res.status_code == 201
        assert "Created" in res_data["status"]
