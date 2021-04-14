import time

from loguru import logger as log

from data.config import auth_info
from liveAnalise.bet_analitics import get_analitics
from loader import driver
from onlinesim import getLastCode, getNewCode


def logInSite_():
    try:

        try:
            file = open('analise_history_bet.txt', 'w')
            file.close()
        except:
            pass

        log.debug('-- Start Login on site --')

        # заходим на страницу
        driver.get('https://1xstavka.ru/en/live/Tennis/')
        time.sleep(2)

        # нажимаем на кнопку "Войти"
        login = driver.find_element_by_xpath('//*[@id="loginout"]/div/div/div/div[1]')
        time.sleep(2)
        login.click()

        username = driver.find_element_by_xpath('//*[@id="auth_id_email"]')
        password = driver.find_element_by_xpath('//*[@id="auth-form-password"]')
        btn = driver.find_element_by_xpath('//*[@id="loginout"]/div/div/div/div[2]/div/form/button')

        username.send_keys(auth_info[0])
        password.send_keys(auth_info[1])
        time.sleep(2)
        btn.click()

        try:
            last_code = getLastCode()
            log.info(f"Last-Code -- [{last_code}]")
            time.sleep(3)
            phone = driver.find_element_by_xpath('//*[@id="phone_middle"]')
            phone.send_keys('90632831')
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/form/button').click()
            driver.refresh()
            time.sleep(3)
            new_code = getNewCode(last_code)
            code = driver.find_element_by_xpath('//*[@id="input_otp"]')
            code.send_keys(new_code)
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/form/button').click()
            time.sleep(3)
            log.debug('Autorization [-OK]')
        except Exception as e:
            pass

        log.debug('Autorization - [OK]')
        time.sleep(5)

        get_analitics(driver)

    except Exception as e:
        log.error(e)
        log.debug('-- Login on site [NOT OK] --')
