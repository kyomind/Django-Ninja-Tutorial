from django.http import HttpRequest
from ninja import Router

from user.models import User
from user.schemas import CreateUserRequest

router = Router()


@router.get(path='/users/', response=list[str], summary='取得所有使用者')
def get_users(request: HttpRequest) -> list[str]:
    users = User.objects.all()
    return [user.username for user in users]


@router.post(path='/users/', summary='新增使用者')
def create_user(request: HttpRequest, payload: CreateUserRequest) -> tuple[int, dict]:
    """
    新增使用者
    """
    user = User.objects.create(
        username=payload.username,
        email=payload.email,
        password=payload.password,
        bio=payload.bio,
    )
    return 201, {'id': user.id, 'username': user.username}
