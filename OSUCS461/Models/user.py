from pydantic import BaseModel

class UserWrite(BaseModel):
	name: str

class User(UserWrite):
	uuid: str
	time_created: int