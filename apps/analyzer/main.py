from fastapi import FastAPI

from controllers.routers.receiver_api import router as receiver_router
from controllers.routers.read_api import router as read_api_router


app = FastAPI()

app.include_router(receiver_router)

app.include_router(read_api_router)
