from abc import ABC
from user_type import UserType
class User(ABC):
    def __init__(self, user_id, type: UserType):
        self.user_id = user_id
        self.type = (type or UserType.USER) # by default type is USER

    def get_type(self):
        return self.type