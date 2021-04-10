
from databases.SQL import SQL

class Database:
    def __new__(self, data):
        if data["type"] == "SQL":
            return SQL(data)
