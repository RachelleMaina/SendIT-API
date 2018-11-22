import pytest
import json
from app import create_app


@pytest.fixture
def app_client():
    """"Method to initialize app and test_client."""
    app = create_app()
    test_client = app.test_client()
    return test_client

order = {"pickup_location": "Nairobi",
          "destination": "Kisumu", "weight": 20}
login_admin = {"username": "Maina", "password": "maina"}
login_user= {"username": "Rachel", "password": "rachel"}
status = {"status": "In Transit"}
location = {"current_location": "Marsabit"}
destination = {"destination": "Malindi"}
signup = {"username": "Rachel", "password": "rachel",
         "phone": 254712345123, "email": "rachellemaina@gmail.com"}


@pytest.fixture
def app_admin(app_client):
    """"Method to test get all orders in the application ."""
    res = app_client.post("/api/v2/auth/login", data=json.dumps(login_admin),
                          content_type='application/json;charset=utf-8')
    access_token = json.loads(res.data)["access_token"]

    return access_token

@pytest.fixture
def app_user(app_client):
    """"Method to test get all orders in the application ."""
    app_client.post("/api/v2/auth/signup", data=json.dumps(signup),
                          content_type='application/json;charset=utf-8')
    res = app_client.post("/api/v2/auth/login", data=json.dumps(login_user),
                          content_type='application/json;charset=utf-8')
    access_token = json.loads(res.data)["access_token"]

    return access_token


class TestOrderViews(object):
    """"Class to test Order delivery views."""
    def test_register(self, app_client):
        """"Method to test if all parcel order deliveries are fetched."""
        res = app_client.post("api/v2/auth/signup", data=json.dumps(signup),
                          content_type="application/json;charset=utf-8")

        res_data = json.loads(res.data.decode())
        assert res.status_code == 201

    def test_login(self, app_client):
        """"Method to test if all parcel order deliveries are fetched."""
        res = app_client.post("api/v2/auth/login", data=json.dumps(signup),
                          content_type="application/json;charset=utf-8")

        res_data = json.loads(res.data.decode())
        assert res.status_code == 200
 



    def test_get_all_orders_in_application(self, app_client, app_admin):
        """"Method to test if all parcel order deliveries are fetched."""
        res = app_client.get("/api/v2/parcels",
                           headers=dict(Authorization="Bearer " + app_admin))

        res_data = json.loads(res.data.decode())
        assert res.status_code == 404

    def test_get_all_orders_by_user(self, app_client, app_user):
        """"Method to test if all parcel order deliveries are fetched."""
        app_client.post("/api/v2/parcels", data=json.dumps(order),
                          content_type="application/json;charset=utf-8",
                           headers=dict(Authorization="Bearer " + app_user))

        res = app_client.get("/api/v2/user/parcels",
                           headers=dict(Authorization="Bearer " + app_user))

        res_data = json.loads(res.data.decode())
        assert res.status_code == 404

    def test_create_order(self, app_client, app_user):
        """"Method to test if all parcel order deliveries are fetched."""
        res = app_client.post("/api/v2/parcels", data=json.dumps(order),
                          content_type="application/json;charset=utf-8",
                           headers=dict(Authorization="Bearer " + app_user))

        res_data = json.loads(res.data.decode())
        assert res.status_code == 400

    def test_change_status(self, app_client, app_admin):
        """"Method to test if all parcel order deliveries are fetched."""
        res = app_client.put("/api/v2/parcels/1/status", data=json.dumps(status),
                          content_type="application/json;charset=utf-8",
                           headers=dict(Authorization="Bearer " + app_admin))

        res_data = json.loads(res.data.decode())
        assert res.status_code == 400

    def test_change_location(self, app_client, app_admin):
        """"Method to test if all parcel order deliveries are fetched."""
        res = app_client.put("/api/v2/parcels/1/presentLocation", data=json.dumps(location),
                          content_type="application/json;charset=utf-8",
                           headers=dict(Authorization="Bearer " + app_admin))

        res_data = json.loads(res.data.decode())
        assert res.status_code == 400

    def test_change_destination(self, app_client, app_user):
        """"Method to test if all parcel order deliveries are fetched."""
        res = app_client.put("/api/v2/parcels/1/destination", data=json.dumps(destination),
                          content_type="application/json;charset=utf-8",
                           headers=dict(Authorization="Bearer " + app_user))

        res_data = json.loads(res.data.decode())
        assert res.status_code == 400


