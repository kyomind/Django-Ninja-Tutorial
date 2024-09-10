from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Router

from post.models import Post

router = Router()


@router.get(path='/posts/')
def get_posts(request: HttpRequest) -> QuerySet[Post]:
    posts = Post.objects.all()
    return posts


@router.get(path='/posts/{int:post_id}/')
def get_post(request: HttpRequest, post_id: int) -> Post:
    post = Post.objects.get(id=post_id)
    return post
