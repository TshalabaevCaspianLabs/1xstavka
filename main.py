import eel


@eel.expose
def start_programm(login, password, koef, bet):
    print([login, password, koef, bet])


eel.init('web')
eel.start('main.html', size=(500, 500))