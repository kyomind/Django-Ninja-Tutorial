from django.http import HttpRequest
from ninja import Router

from .models import User

router = Router()


@router.get(path='/users/', response=list[str], summary='取得所有使用者')
def get_users(request: HttpRequest) -> list[str]:
    users = User.objects.all()
    return [user.username for user in users]
