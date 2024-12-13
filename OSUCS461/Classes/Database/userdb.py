from OSUCS461.Classes.Database import DB
from OSUCS461.Models.user import User, UserWrite
from OSUCS461.Utilities import createHash, nowSeconds

class UserDB:
    table = "user"

    @staticmethod
    def create(user: UserWrite) -> str:
        uuid = createHash(UserDB.table)
        result = DB.Add(table=UserDB.table, data={"uuid": uuid, "name": user.name, "time_created": nowSeconds()})

        return result["uuid"]

    @staticmethod
    def get_all() -> list[User]:
        result = DB.GetAll(UserDB.table)

        return list(map(lambda r: User(**r), result))

    @staticmethod
    def get(uuid: str) -> User:
        result = DB.GetBy(UserDB.table, field_params={"uuid": uuid})

        return User(**result)

    @staticmethod
    def update(uuid: str, user: UserWrite) -> bool:
        return DB.Update(UserDB.table, data={"name": user.name}, field_params={"uuid": uuid})

    @staticmethod
    def delete(uuid: str) -> bool:
        result = DB.DeleteWhere(UserDB.table, field_params={"uuid": uuid})

        return result["result"]