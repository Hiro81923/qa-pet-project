import pytest
import requests
from dotenv import load_dotenv
import os

BASE_URL = "https://reqres.in"

@pytest.mark.api
def test_create_user_success_api():
    payload = {
        "name": "Just User",
        "job": "AQA Engineer"
    }
    
    response = requests.post(f"{BASE_URL}/api/users", json=payload)

    assert response.status_code == 201
    
    response_body = response.json()
    assert response_body.get("name") == "Just User"
    assert response_body.get("job") == "AQA Engineer"


@pytest.mark.api
def test_register_new():
    payload = {
        "email": "eve.holt@reqres.in",  
        "password": "psswd"
    }

    response = requests.post(f"{BASE_URL}/api/register", json=payload)

    assert response.status_code == 200

    response_body = response.json()
    assert "id" in response_body
    assert "token" in response_body
    assert response_body.get("id") is not None


@pytest.mark.api
def test_register_missing_password_api():
    payload = {
        "email": "eve.holt@reqres.in"
    }
    
    response = requests.post(f"{BASE_URL}/api/register", json=payload)

    assert response.status_code == 400
    
    response_body = response.json()
    assert response_body.get("error") == "Missing password"

load_dotenv()

PASSWORD = os.getenv("MY_PASSWORD")

@pytest.mark.api
def test_successful_login_with_custom_password():
    payload = {
        "email": "eve.holt@reqres.in", 
        "password": PASSWORD        
    }
    
    response = requests.post(f"{BASE_URL}/api/login", json=payload)

    assert response.status_code == 200
    
    response_body = response.json()
    assert "token" in response_body
    assert response_body.get("token") is not None
