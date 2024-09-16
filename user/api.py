from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Router

from .models import User

router = Router()


@router.get(path='/users/')
def get_users(request: HttpRequest) -> list[str]:
    users = User.objects.all()
    return [user.username for user in users]
