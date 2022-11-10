# imports
from tkinter import *
import os
from PIL import Image, ImageTk


class BankAccount:
    id = 1  # Class Attribute

    def __init__(self, user_login, user_pass, balance=0):
        self.user_login = user_login
        self.user_pass = user_pass
        self.balance = balance
        self.accountNumber = BankAccount.id + 1
        self.create_account()
        print(f'Создан пользователь с именем {self.user_login} и паролем {self.user_pass}')

    def create_account(self):
        all_accounts = os.listdir()
        if self.user_login == '' or self.user_pass == '':
            notif.config(fg='red', text='Заполните все поля!')
            return
        for name in all_accounts:
            if self.user_login == name:
                notif.config(fg='red', text='Аккаунт уже существует!')
                return
        notif.config(text='')
        with open(self.user_login, 'w') as f:
            f.write(f'{self.user_login}\n'
                    f'{self.user_pass}\n'
                    f'{self.balance}')
        notif.config(fg='green', text='Аккаунт успешно создан!')

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print('Not enough balance!')
        else:
            self.balance -= amount

    def getBalance(self):
        return self.balance


# Создание окна
main = Tk()  # создаем корневой объект - окно
main.title('Banking System')  # устанавливаем заголовок окна
main.geometry("300x300")  # устанавливаем размеры окна


def create_user():
    login = user_login.get()
    password = user_pass.get()
    BankAccount(login, password)


# Register and login
def register():
    # Variables
    global user_login
    global user_pass
    global notif

    user_login = StringVar()
    user_pass = StringVar()

    register_screen = Toplevel(main)
    register_screen.geometry('300x300+500+500')
    register_screen.title('Register')

    # Labels
    Label(register_screen, text='Please enter your details below to register', font=('Calibri', 12)).grid(row=0,
                                                                                                          sticky=N,
                                                                                                          pady=10)
    Label(register_screen, text='Name', font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(register_screen, text='Password', font=('Calibri', 12)).grid(row=2, sticky=W)
    notif = Label(register_screen, font=('Calibri', 12))
    notif.grid(row=4, sticky=N, pady=10)

    # Entries
    Entry(register_screen, textvariable=user_login).grid(row=1, column=0)
    Entry(register_screen, textvariable=user_pass, show='*').grid(row=2, column=0)

    # Creating register button
    Button(register_screen, text='Register', font=('Calibri', 12), width=15,
           command=create_user).grid(row=3, column=0,
                                     pady=20)


def login():
    # Login Screen
    login_screen = Toplevel(main)
    login_screen.title('Login')

    # Labels
    Label(login_screen, text='Login to your account', font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(login_screen, text='Username', font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(login_screen, text='Password', font=('Calibri', 12)).grid(row=2, sticky=W)
    # Entries
    Entry(login_screen, textvariable=user_login).grid(row=1, column=0)
    Entry(login_screen, textvariable=user_pass, show='*').grid(row=2, column=0)


# Создание картинки
img = Image.open('data/img/bank.PNG')  # открываем изображение
img = img.resize((150, 150))  # задаем размер
img = ImageTk.PhotoImage(img)

# Labels
Label(main, text='Самый безопасный банк').pack(side=TOP)
Label(main, image=img).pack(side=TOP)

# Buttons
Button(main, text='Register', font=('Calibri', 12), width=15, command=register).pack(side=TOP, pady=10)
Button(main, text='Login', font=('Calibri', 12), width=15, command=login).pack(side=TOP)

main.mainloop()  # запускаем цикл обработки событий окна для взаимодействия с пользователем
