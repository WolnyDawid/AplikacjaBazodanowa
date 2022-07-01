import sqlite3


class dbInitialization:
    def __init__(self, databaseName):
        self.var = None
        self.connection = sqlite3.connect(databaseName)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def insert(self, table, *values):
        self.cursor.execute(f'INSERT INTO {table} (name, surrname, email) VALUES (?,?,?)', values)
        self.connection.commit()

    def return_record(self, table, *existingValues):
        self.cursor.execute(f'SELECT * FROM {table} WHERE name= ? and surrname= ?', existingValues)
        self.var = self.cursor.fetchone()
        return self.var
