from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpRequest, HttpResponse
from ninja import NinjaAPI

api = NinjaAPI(
    title='忍者論壇 API', version='1.0', description='這是忍者論壇的 API 文件，供讀者參考'
)

api.add_router(prefix='', router='user.api.router', tags=['User'])
api.add_router(prefix='', router='post.api.router', tags=['Post'])


@api.exception_handler(exc_class=ValidationError)
def django_validation_error_handler(
    request: HttpRequest, exception: ValidationError
) -> HttpResponse:
    """
    處理 Django ValidationError 例外
    """
    return api.create_response(request, {'detail': exception.message}, status=400)


@api.exception_handler(exc_class=ObjectDoesNotExist)
def object_does_not_exist_handler(
    request: HttpRequest, exception: ObjectDoesNotExist
) -> HttpResponse:
    """
    處理 Django ObjectDoesNotExist 例外
    """
    return api.create_response(request, {'detail': '查無資料'}, status=404)
