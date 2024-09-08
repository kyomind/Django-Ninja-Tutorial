from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Router

from .models import User

router = Router()


@router.get(path='/')
def get_users(request: HttpRequest) -> QuerySet[User]:
    users = User.objects.all()
    return users
