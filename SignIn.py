from dbInitialization import dbInitialization


class SignIn:

    def logowanie(self, name, surrname, table, dbName):
        db = dbInitialization(dbName)
        db.create_table(f'CREATE TABLE IF NOT EXISTS {table} (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, surrname text, email text)')
        row = db.return_record('users', name, surrname)
        if not row:
            print('Nie zalogowano')
        else:
            print('Zalogowano')