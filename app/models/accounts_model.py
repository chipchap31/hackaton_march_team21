from ..DB import Database
from datetime import datetime
class AccountsModel(Database):
    def __init__(self):
        self.default = {
            'f_name': '',
            'l_name': '',
            'created_at': datetime.now()
        }