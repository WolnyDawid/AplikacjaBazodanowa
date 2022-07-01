from AddNewUser import *
from SignIn import *
import tkinter

print('Witaj w xyzqqqq')
print('Menu')
print('1. Logowanie')
print('2. Dodaniue nowego urzytkownika')
print('3. Wyjście')

dbName = "baza_uzytkownikaow.db"
table = 'users'


main = tkinter.Tk()
existingUserNameInput = tkinter.Entry(main)
existingUserSurrnameInput = tkinter.Entry(main)


existingUserNameInput.pack()
existingUserSurrnameInput.pack()
main.mainloop()

# while b <= 3:
#     try:
#         b = int(input("Wybór: "))
#     except ValueError:
#         print("Wprowadzono błędne dane, podaj wybór: \n"
#               "1. Logowanie, \n"
#               "2. Tworzneie nowego użytkownika, \n"
#               "3. Wyjście \n")

    # if b == 1:
existingUserName = input("Podaj imię użytkownika: ")
existingUserSurrname = input("Podaj nazwisko: ")
SignIn().logowanie(existingUserName, existingUserSurrname, table, dbName)

    # elif b == 2:
def logowanie():
    userName = input("Podaj imię użytkownika: ")
    userSurrname = input("Podaj nazwisko: ")
    addNewUser().dodanieNowegoUzytkownika(userName, userSurrname, table, dbName)


