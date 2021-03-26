from tkinter import *
from login import logInSite

def tkinter_gui():
    root = Tk()
    root.title("Bot 1xstavkaPy 🐬")
    root.geometry("400x400")
    root["bg"] = "gray22"

    sum = StringVar()

    sum_entry = Entry(textvariable=sum)
    name_title = Label(text="Введите сумму ставки: =>")
    name_title.grid(row=0, column=0, sticky="w")
    sum_entry.grid(row=0,column=1, padx=5, pady=5)


    message_button = Button(text="Начать", command=logInSite(sum.get()))
    message_button.place(relx=.5, rely=.7, anchor="c")




    root.mainloop()