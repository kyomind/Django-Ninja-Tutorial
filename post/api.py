from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Query, Router
from ninja.pagination import PageNumberPagination, paginate

from post.models import Post
from post.schemas import CreatePostRequest, PostListResponse, PostResponse

router = Router()


@router.get(path='/posts/', response=list[PostListResponse], summary='取得文章列表')
@paginate(PageNumberPagination, page_size=10)
def get_posts(
    request: HttpRequest,
    title: None | str = Query(None, min_length=2, max_length=10),
) -> QuerySet[Post]:
    """
    取得文章列表
    """
    posts = Post.objects.all()
    if title:
        posts = posts.filter(title__icontains=title).select_related('author')
    return posts


@router.get(path='/posts/{int:post_id}/', response=PostResponse, summary='取得單一文章資訊')
def get_post(request: HttpRequest, post_id: int) -> Post:
    """
    取得單一文章資訊
    """
    post = Post.objects.get(id=post_id)
    return post


@router.post(path='/posts/', response={201: dict}, summary='新增文章')
def create_post(request: HttpRequest, payload: CreatePostRequest) -> tuple[int, dict]:
    """
    新增文章
    """
    post = Post.objects.create(
        title=payload.title,
        content=payload.content,
        author_id=payload.user_id,
    )
    return 201, {'id': post.id, 'title': post.title}
