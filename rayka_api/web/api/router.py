from fastapi.routing import APIRouter

from rayka_api.web.api import docs, dummy, echo, monitoring, users

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(users.router)
api_router.include_router(docs.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
# api_router.include_router(redis.router, prefix="/redis", tags=["redis"]) # noqa
# api_router.include_router(rabbit.router, prefix="/rabbit", tags=["rabbit"]) # noqa
