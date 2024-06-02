import pytest
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'

def test_get_posts():
    response = requests.get(f'{BASE_URL}/posts')
    assert response.status_code == 200
    assert len(response.json()) == 100  # JSONPlaceholder has 100 posts

def test_get_single_post():
    response = requests.get(f'{BASE_URL}/posts/1')
    assert response.status_code == 200
    assert response.json().get('id') == 1

def test_create_post():
    new_post = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1,
    }
    response = requests.post(f'{BASE_URL}/posts', json=new_post)
    assert response.status_code == 201
    response_data = response.json()
    assert 'id' in response_data
    for key in new_post:
        assert response_data[key] == new_post[key]

def test_update_post():
    updated_post = {
        'title': 'foo updated',
        'body': 'bar updated',
        'userId': 1,
    }
    response = requests.put(f'{BASE_URL}/posts/1', json=updated_post)
    assert response.status_code == 200
    response_data = response.json()
    for key in updated_post:
        assert response_data[key] == updated_post[key]

def test_delete_post():
    response = requests.delete(f'{BASE_URL}/posts/1')
    assert response.status_code == 200
    assert response.json() == {}