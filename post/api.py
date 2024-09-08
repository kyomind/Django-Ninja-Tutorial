from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Router

from post.models import Post

router = Router()


@router.get(path='/')
def get_posts(request: HttpRequest) -> QuerySet[Post]:
    posts = Post.objects.all()
    return posts
