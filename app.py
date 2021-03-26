import time
from tkinter import *
from auth import logInSite


if __name__ == '__main__':
    root = Tk()
    root.title("Bot 1xstavkaPy 🐬")
    root.geometry("400x400")
    root["bg"] = "gray22"

    def start_driver():
        logInSite(sum.get())
    
    sum = StringVar()

    sum_entry = Entry(textvariable=sum)
    name_title = Label(text="Введите сумму ставки: =>")
    name_title.grid(row=0, column=0, sticky="w")
    sum_entry.grid(row=0, column=1, padx=5, pady=5)

    message_button = Button(text="Начать", command=start_driver)
    message_button.place(relx=.5, rely=.7, anchor="c")

    root.mainloop()
    time.sleep(10)
