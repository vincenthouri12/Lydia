import requests
import pytest
import allure

BASE_URL = "https://reqres.in/api"
API_KEY = "reqres-free-v1"

HEADERS = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

REGISTER_PAYLOAD = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

user_id = None

# ---------------------
#  REGISTER
# ---------------------
@allure.feature("User API")
@allure.story("Register user")
def test_register_user():
    global user_id

    response = requests.post(
        f"{BASE_URL}/register",
        json=REGISTER_PAYLOAD,
        headers=HEADERS
    )
    assert response.status_code == 200
    data = response.json()

    assert "id" in data
    assert "token" in data

    user_id = data["id"]


# -----------------
#  GET USER
# -----------------
@allure.feature("User API")
@allure.story("Get user")
def test_get_user():
    assert user_id is not None

    response = requests.get(
        f"{BASE_URL}/users/{user_id}",
        headers=HEADERS
    )

    assert response.status_code == 200
    data = response.json()

    assert "data" in data
    assert data["data"]["id"] == user_id


# ----------------------
# MISSING PSWD
# ----------------------
@allure.story("Register user missing password")
def test_register_missing_password():
    response = requests.post(
        f"{BASE_URL}/register",
        json={"email": "eve.holt@reqres.in"},
        headers=HEADERS
    )
    assert response.status_code == 400
    data = response.json()
    assert data["error"] == "Missing password"


# ----------------------
# MISSING EMAIL 
# ----------------------
@allure.story("Register user missing email")
def test_register_missing_email():
    response = requests.post(
        f"{BASE_URL}/register",
        json={"password": "pistol"},
        headers=HEADERS
    )
    assert response.status_code == 400
    data = response.json()
    assert data["error"] == "Missing email or username"


# ----------------------
# USER NOT FOUND
# ----------------------
@allure.story("get unknown user")
def test_get_unknown_user():
    response = requests.get(
        f"{BASE_URL}/users/999999",
        headers=HEADERS
    )
    assert response.status_code == 404
