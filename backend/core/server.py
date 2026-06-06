from fastapi import FastAPI

from api import router


def init_routers(app: FastAPI) -> None:
    app.include_router(router)

def server() -> FastAPI:
    app_ = FastAPI(
        title="MarketPlace Platform API",
        description="API for the MarketPlace Platform",
        version="1.0.0",
    )
    init_routers(app_)
    return app_