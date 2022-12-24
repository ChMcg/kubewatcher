from pydantic import BaseModel


class DBConnectionModel(BaseModel):
    user: str
    password: str
    host: str
    port: str

    def __init__(__pydantic_self__, data: dict) -> None:
        super().__init__(**data)
