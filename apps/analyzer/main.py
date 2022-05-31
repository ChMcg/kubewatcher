
from fastapi import FastAPI

from receiver import router as receiver_router
from read_api import router as read_api_router


app = FastAPI()
app.include_router(receiver_router)
app.include_router(read_api_router)






