import logging

import pytest
from django.test import Client

from user.models import User

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


@pytest.fixture(scope='session')
def client() -> Client:
    """
    返回 Django 測試用的 client

    補充說明：
    pytest-django 本來就有提供 client fixture，這裡是為了示範如何自訂 client fixture
    請留意這個 client fixture 是 session scope，也就是整個測試過程只會建立一次
    """
    return Client()


@pytest.fixture
def user() -> User:
    """
    建立使用者並返回
    """
    return User.objects.create_user(
        username='testuser', email='testuser@example.com', password='testpassword123'
    )


@pytest.fixture
def authenticated_client(client: Client, user: User) -> Client:
    """
    登入並返回已認證的 client
    """
    response = client.post(
        '/users/login/',
        {'username': 'testuser', 'password': 'testpassword123'},
        content_type='application/json',
    )
    logger.info(response.json())
    assert response.status_code == 200
    # 設定登入後的 cookies
    client.cookies.update(response.cookies)
    return client
