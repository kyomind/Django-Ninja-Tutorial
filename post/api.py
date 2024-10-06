from django.db.models import QuerySet
from django.http import HttpRequest
from ninja import Query, Router
from ninja.pagination import paginate

from NinjaForum.pagination import CustomPagination
from post.models import Post
from post.schemas import CreatePostRequest, PostFilterSchema, PostListResponse, PostResponse

router = Router()


@router.get(path='/posts/', response=list[PostListResponse], summary='取得文章列表')
@paginate(CustomPagination)
def get_posts(
    request: HttpRequest,
    filters: PostFilterSchema = Query(),
) -> QuerySet[Post]:
    """
    取得文章列表
    """
    posts = Post.objects.select_related('author')
    posts = filters.filter(posts)
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
