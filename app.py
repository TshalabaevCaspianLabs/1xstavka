from auth import logInSite
import eel


@eel.expose
def start_programm(login, password, koef, bet):

    data = [[f'{login}', f'{password}', f'{koef}', f'{bet}']]
    logInSite(data[0])



eel.init('web')
eel.start('main.html', size=(500, 500))