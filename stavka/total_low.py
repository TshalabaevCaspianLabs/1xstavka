import time

from loguru import logger


def place_bet(driver, urls, sum_price):
    for url in urls:
        try:
            number_1 = url.split('https://1xstavka.ru/en/live/Tennis/')[1].split('/')[0]
            number_main = url.split(f"{number_1}" + '/')[1].split('-')[0]
            driver.get(url)
            time.sleep(2)
            driver.find_element_by_class_name('scoreboard-nav__select').click()
            time.sleep(2)
            driver.find_element_by_xpath(
                f'//*[@id="{int(number_main)}"]/div[1]/div[3]/div/div[1]/div[1]/div/div[3]/ul/li[2]').click()
            time.sleep(4)

            divs = driver.find_elements_by_tag_name('div')
            for div in divs:
                try:
                    if div.get_attribute('class') == 'bets betCols2':
                        span_list = div.find_elements_by_tag_name('span')
                        for span in span_list:
                            if span.text == 'Total Under 10.5' or span.text == 'Under 10.5':
                                try:
                                    driver.find_element_by_xpath('//*[@id="sports_right"]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div[1]/button').click()
                                except:
                                    pass

                                span.click()
                                time.sleep(1)
                                break
                except:
                    pass
            time.sleep(1)
            price = driver.find_element_by_xpath(
                '//*[@id="sports_right"]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]/div/div[3]/div/input')
            price.send_keys(f'{sum_price}')
            time.sleep(2)
            driver.find_element_by_xpath(
                '//*[@id="sports_right"]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[3]/div/div/div/button').click()
            time.sleep(5)
            logger.debug('--[Accept Bet]--')
        except:
            pass
