from dbInitialization import dbInitialization

specialCharacters = """!@\#$%^&*()_+=-[]{};'"/~?.,<> """


class addNewUser:

    def dodanieNowegoUzytkownika(self, name, surrname, table, dbName):
        if any(iName.isnumeric() for iName in name) or any(cName in specialCharacters for cName in name):
            print("Wprowadź poprawne imię:litery bez cyfer, znaków specjalnych")
        elif len(name) < 2:
            print("Imię użytkownika musi składać się przynajmniej z 2 znaków")
        elif any(iSurr.isnumeric() for iSurr in surrname) or any(
                cSurr in specialCharacters for cSurr in surrname):
            print("Wprowadź poprawne naziwsko: litery bez cyfer, znaków specjalnych")
        elif len(surrname) < 2:
            print("Nazwisko użytkownika musi składać się przynajmniej z 2 znaków")
        else:
            db = dbInitialization(dbName)
            db.create_table(f'CREATE TABLE IF NOT EXISTS {table} (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, surrname text, email text)')

            email = name + "." + surrname + "@firma.com"
            db.insert('users', name, surrname, email)
        return name, surrname


