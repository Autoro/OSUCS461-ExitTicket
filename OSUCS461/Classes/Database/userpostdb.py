from OSUCS461.Classes.Database import DB
from OSUCS461.Models.userpost import UserPost, UserPostWrite
from OSUCS461.Utilities import createHash, nowSeconds

class UserPostDB:
    table = "user_post"

    @staticmethod
    def create(user_uuid: str, post: UserPostWrite) -> str:
        uuid = createHash(UserPostDB.table)
        result = DB.Add(UserPostDB.table, data={
            "uuid": uuid,
            "user_uuid": user_uuid,
            "post_9char": post.text[:9],
            "text": post.text,
            "time_created": nowSeconds()
        })

        return result["uuid"]

    @staticmethod
    def get_all(user_uuid: str):
        result = DB.GetAllWhere(UserPostDB.table, field_params={"user_uuid": user_uuid})

        return list(map(lambda r: UserPost(**r), result))

    @staticmethod
    def get(user_uuid: str, uuid: str) -> UserPost:
        result = DB.GetBy(UserPostDB.table, field_params={"uuid": uuid, "user_uuid": user_uuid})

        return UserPost(**result)

    @staticmethod
    def delete(user_uuid: str, uuid: str) -> bool:
        result = DB.DeleteWhere(UserPostDB.table, field_params={"uuid": uuid, "user_uuid": user_uuid})

        return result["result"]