from .user_type import UserType
from .user import User
class Customer(User):
    def __init__(self, user_id, type: UserType):
        super().__init__(user_id, type)