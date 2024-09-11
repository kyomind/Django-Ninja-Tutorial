from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Query, Router

from post.models import Post

router = Router()


@router.get(path='/posts/')
def get_posts(
    request: HttpRequest,
    title: None | str = Query(None, min_length=2, max_length=10),
) -> QuerySet[Post]:
    posts = Post.objects.all()
    if title:
        posts = posts.filter(title__icontains=title)
    return posts


@router.get(path='/posts/{int:post_id}/')
def get_post(request: HttpRequest, post_id: int) -> Post:
    post = Post.objects.get(id=post_id)
    return post
