from ninja import NinjaAPI

api = NinjaAPI()

api.add_router(prefix='', router='user.api.router', tags=['User'])
api.add_router(prefix='', router='post.api.router', tags=['Post'])
