import time
from tkinter import *
from auth import logInSite


if __name__ == '__main__':
    root = Tk()
    root.title("Bot 1xstavkaPy 🐬")
    root.geometry("500x500")
    root["bg"] = "gray22"

    OptionList = [
        "Under 10.5",
        "Under 9.5",
        "Under 8.5"
    ]

    def start_driver(*args):
        logInSite(sum.get(), variable.get())

    sum = StringVar()
    sum_entry = Entry(textvariable=sum)
    name_title = Label(text="Введите коэф в формате (1.2, 3.0)=>")
    name_title.grid(row=0, column=0, sticky="w")
    sum_entry.grid(row=0, column=1, padx=5, pady=5)

    variable = StringVar(root)
    variable.set(OptionList[0])

    opt = OptionMenu(root, variable, *OptionList)
    opt.config(width=90, font=('Helvetica', 12))
    opt.place(relx=.5, rely=.5, anchor="c")

    variable.trace("w", start_driver)

    # message_button = Button(text="Начать", command=start_driver)
    # message_button.place(relx=.5, rely=.7, anchor="c")

    root.mainloop()
    time.sleep(10)
