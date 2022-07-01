from dbInitialization import dbInitialization

print('Witaj w xyzqqqq')
print('Menu')
print('1. Logowanie')
print('2. Dodaniue nowego urzytkownika')
print('3. Wyjście')
b = 0
specialCharacters = """!@\#$%^&*()_+=-[]{};'"/~?.,<> """


def dodanieNowegoUzytkownika():
        userName = input("Podaj imię użytkownika: ")
        userSurname = input("Podaj nazwisko: ")
        if any(iName.isnumeric() for iName in userName) or any(cName in specialCharacters for cName in userName):
            print("Wprowadź poprawne imię:litery bez cyfer, znaków specjalnych")
        elif len(userName) < 2:
            print("Imię użytkownika musi składać się przynajmniej z 2 znaków")
        elif any(iSurr.isnumeric() for iSurr in userSurname) or any(cSurr in specialCharacters for cSurr in userSurname):
            print("Wprowadź poprawne naziwsko: litery bez cyfer, znaków specjalnych")
        elif len(userSurname) < 2:
            print("Nazwisko użytkownika musi składać się przynajmniej z 2 znaków")
        else:
            newUsersEmail = userName + "." + userSurname + "@firma.com"
            db.insert('users', userName, userSurname, newUsersEmail)
        return userName, userSurname


def logowanie():
    userName = input("Podaj imię użytkownika: ")
    userSurrname = input("Podaj nazwisko: ")
    row = db.return_record('users', userName, userSurrname)
    if not row:
        print('Nie zalogowano')
    else:
        print('Zalogowano')


while b <= 3:
    try:
        b = int(input("Wybór: "))
    except ValueError:
        print("Wprowadzono błędne dane, podaj wybór: \n"
              "1. Logowanie, \n"
              "2. Tworzneie nowego użytkownika, \n"
              "3. Wyjście \n")
    else:
        db = dbInitialization("baza_uzytkownikaow.db")
        db.create_table('''CREATE TABLE IF NOT EXISTS users
                                        (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, surrname text, email text)''')

    if b == 1:
        print("dupa1")
        logowanie()
    elif b == 2:
        print("dupa2")
        dodanieNowegoUzytkownika()


