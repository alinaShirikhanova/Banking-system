# imports
from tkinter import *
import os
from PIL import Image, ImageTk

# Создание окна
main = Tk()  # создаем корневой объект - окно
main.title('Banking System')  # устанавливаем заголовок окна


# Register and login
def register():
    register_screen = Toplevel(main)


main.geometry("300x300")  # устанавливаем размеры окна

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
