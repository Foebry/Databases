import os
import sys


class Database:
    def __new__(self, data, logger):
        if data["type"] == "MySQL":

            try: import mysql
            except: os.system("pip install mysql-connector")

            from databases.SQL import SQL
            return SQL(data, logger)
