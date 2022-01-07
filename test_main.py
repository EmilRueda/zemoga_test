import pytest

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def fixture_connection_twitter():
    valid_twitter_user_id_example = "@elonmusk"
    wrong_twitter_user_id_example = "5ggt6ya"
    users = [
        valid_twitter_user_id_example,
        wrong_twitter_user_id_example
    ]
    return users

def test_connection_twitter_valid_user(fixture_connection_twitter):
    response = client.get(url="/tweets/" + fixture_connection_twitter[0])
    assert response.status_code == 200
    
def test_connection_twitter_wrong_user(fixture_connection_twitter):
    
    response = client.get(url="/tweets/" + fixture_connection_twitter[1])
    assert response.status_code == 404

def test_login_request():
    response = client.get(url="/login")
    assert response.status_code == 200
    
def show_user_request_valid_user():
    response = client.get(url="/user/123")
    assert response.status_code == 200
    
def show_user_request_wrong_user():
    response = client.get(url="/user/er56gf")
    assert response.status_code == 404

def update_user():
    response = client.put(url="/user/123/update", json={
        "idportfolio": 3,
        "description": "I am Jack",
        "experience_summary": "I have two years of experience",
        "id": 1010101,
        "image_url": "http://kingdomhearts.fandom.com/es/wiki/Jack_Skeleton?fil:Jack_Skeleton_KHII.png",
        "last_names": "Gordon",
        "names": "Jack",
        "tittle": "manager",
        "twitter_user_id": "@JackGordon",
        "twitter_user_name": "Jack Gordon",
        "user_id": "123"
    })
    assert response.status_code == 200

def update_user():
    response = client.put(url="/user/456/update", json={
        "idportfolio": 3,
        "description": "I am Jack",
        "experience_summary": "I have two years of experience",
        "id": 1010101,
        "image_url": "http://kingdomhearts.fandom.com/es/wiki/Jack_Skeleton?fil:Jack_Skeleton_KHII.png",
        "last_names": "Gordon",
        "names": "Jack",
        "tittle": "manager",
        "twitter_user_id": "@JackGordon",
        "twitter_user_name": "Jack Gordon",
        "user_id": "123"
    })
    assert response.status_code == 403

def update_user():
    response = client.put(url="/user/123/update", json={})
    assert response.status_code == 404