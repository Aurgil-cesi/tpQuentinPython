import mysql.connector
from os import path

class Database:

    def __init__(self, host, user, password, database_name):

        self.db = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database_name,
            auth_plugin = "mysql_native_password"
        )
        self._sql_folder = f"{path.dirname(path.realpath(__file__))}/sql"

        self.create()
        # self.fill()

    def execute_sql_file(self, file):

        (connection, cursor) = self.connect()
        file = open(file)
        sql = file.read()
        file.close()
        sql_commands = sql.split(";")

        for sql_command in sql_commands:
            cursor.execute(sql_command)

        connection.commit()

    def create(self):
        self.execute_sql_file(f"{self._sql_folder}/tables.sql")

    def fill(self):
        # self.execute_sql_file(f"{self._sql_folder}/data.sql")

        (connection, cursor) = self.connect()

        for y in range(30):
            for x in range(30):
                cursor.execute(f"insert into cell (x, y, color) values ({x}, {y}, 0)")

        connection.commit()

    def connect(self):
        return (self.db, self.db.cursor())