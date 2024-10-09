import pytest
from django.test import Client

from user.models import User

pytestmark = pytest.mark.django_db


def test_get_users(authenticated_client: Client, user: User) -> None:
    response = authenticated_client.get('/users/')
    assert response.status_code == 200


def test_create_user(client: Client) -> None:
    response = client.post(
        '/users/',
        data={
            'username': 'testuser2',
            'email': 'testuser2@example.com',
            'password': 'testpassword2123',
            'confirm_password': 'testpassword2123',
        },
        content_type='application/json',
    )
    assert response.status_code == 201


def test_login_user(client: Client, user: User) -> None:
    response = client.post(
        '/users/login/',
        data={'username': 'testuser', 'password': 'testpassword123'},
        content_type='application/json',
    )
    assert response.status_code == 200
