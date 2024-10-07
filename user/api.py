from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from ninja import File, Router, UploadedFile
from ninja.errors import HttpError
from ninja.security import django_auth

from user.models import User
from user.schemas import CreateUserRequest, LoginRequest

router = Router()


@router.get(path='/users/', response=list[str], summary='取得所有使用者')
def get_users(request: HttpRequest) -> list[str]:
    users = User.objects.all()
    return [user.username for user in users]


@router.post(path='/users/', response={201: dict}, summary='新增使用者')
def create_user(request: HttpRequest, payload: CreateUserRequest) -> tuple[int, dict]:
    """
    新增使用者
    """
    if User.objects.filter(email=payload.email).exists():
        raise HttpError(409, '使用者 email 已存在')

    user = User(
        username=payload.username,
        email=payload.email,
        bio=payload.bio,
    )
    user.set_password(raw_password=payload.password)  # 使用 set_password 方法加密密碼
    user.save()
    return 201, {'id': user.id, 'username': user.username}


@router.post(path='/users/{int:user_id}/avatar/', summary='上傳 avatar', auth=django_auth)
def upload_avatar(
    request: HttpRequest, user_id: int, avatar_file: UploadedFile = File()
) -> dict[str, str]:
    """
    上傳 avatar
    """
    # 檢查登入的使用者是否為「本人」
    if request.auth.id != user_id:
        raise HttpError(403, '無權限上傳其他使用者的 avatar')

    # 檢查檔案類型
    if not avatar_file.content_type.startswith('image/'):
        raise HttpError(400, '檔案必須是圖片格式')

    user = User.objects.get(id=user_id)
    user.avatar = avatar_file
    user.save()
    return {'detail': '圖片上傳成功'}


@router.post(path='/users/login/', summary='登入使用者')
def login_user(request: HttpRequest, payload: LoginRequest) -> dict[str, str]:
    """
    登入使用者
    """
    user = authenticate(request, username=payload.username, password=payload.password)
    if user is not None:
        login(request, user)  # 將使用者登入狀態保存至 session
        return {'message': '登入成功'}
    else:
        raise HttpError(401, '帳號或密碼錯誤')
