from ninja import NinjaAPI

api = NinjaAPI(
    title='忍者論壇 API', version='1.0', description='這是忍者論壇的 API 文件，供讀者參考'
)

api.add_router(prefix='', router='user.api.router', tags=['User'])
api.add_router(prefix='', router='post.api.router', tags=['Post'])
