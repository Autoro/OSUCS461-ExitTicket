from pydantic import BaseModel

class UserPostWrite(BaseModel):
    text: str

class UserPost(UserPostWrite):
    uuid: str
    user_uuid: str
    post_9char: str
    time_created: int