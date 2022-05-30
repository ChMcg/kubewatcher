
from fastapi import FastAPI

from receiver import router as receiver_router


app = FastAPI()
app.include_router(receiver_router)






