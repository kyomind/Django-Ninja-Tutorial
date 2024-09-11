from ninja import NinjaAPI

api = NinjaAPI()

api.add_router(prefix='', router='user.api.router')
api.add_router(prefix='', router='post.api.router')
