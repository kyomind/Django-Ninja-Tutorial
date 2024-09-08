from ninja import NinjaAPI

api = NinjaAPI()

api.add_router(prefix='/users/', router='user.api.router')
api.add_router(prefix='/posts/', router='post.api.router')
