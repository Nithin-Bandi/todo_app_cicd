import pytest
import sys
import os

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    print(f"test {response}")
    assert response.status_code == 200
    assert b'To-Do List' in response.data

def test_add_task(client):
    response = client.post('/add', data={
        'title': 'Test Task',
        'description': 'Test Description',
        'status': 'Pending'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Test Task' in response.data
