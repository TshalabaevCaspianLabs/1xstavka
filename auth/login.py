import time

from loguru import logger as log

from data.config import auth_info
from liveAnalise.get_link_for_math import get_link_math
from loader import driver
from onlinesim import getLastCode, getNewCode
from stavka.Under_Ten import place_bet


def logInSite(data_auth):
    try:
        try:
            file = open('analytics_file.txt', 'w')
            file.close()
        except:
            pass

        log.debug('-- Start Login on site --')

        # заходим на страницу
        driver.get('https://1xstavka.ru/en/live/Tennis/')
        time.sleep(2)

        # нажимаем на кнопку "Войти"
        login_ = driver.find_element_by_xpath('//*[@id="loginout"]/div/div/div/div[1]')
        time.sleep(2)
        login_.click()

        username = driver.find_element_by_xpath('//*[@id="auth_id_email"]')
        password = driver.find_element_by_xpath('//*[@id="auth-form-password"]')
        btn = driver.find_element_by_xpath('//*[@id="loginout"]/div/div/div/div[2]/div/form/button')

        username.send_keys(data_auth[0])
        password.send_keys(data_auth[1])
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

        # Что бы выставить быструю ставку на сумму что нужна, програмно сделать трудно так как программа
        # не видит окошко с быстрой ставкой
        log.debug('-- Login on site [OK] --')
        log.debug('Start sleep programm, for place last a bet on site')
        time.sleep(10)
        log.debug('Last bet accepted')

        # Сам цикл работы программы, бесконечный
        while True:
            data = get_link_math(driver)
            log.info(f"-- Count Math -> {len(data[0])} --")
            if len(data[0]) == 0:
                data = get_link_math(driver)
            place_bet(driver, data[0], data[1], data[2], data[3])

            time.sleep(30)

    # Обработчик ошибки, на случай если программа не смогла авторизоваться сама
    except Exception as e:
        log.error(e)
        log.debug('-- Login on site [NOT OK] --')
        log.debug('-- Restart a the programm --')
        logInSite()
