import time

from loguru import logger


def read_analitics_file():
    data = []
    with open('/Users/macbookpro/Documents/1xstavka/analytics_file.txt', 'r') as filename:
        for player in filename:
            player = player.strip()
            one, two, bet, set_ = player.split(' | ')
            data.append([one, two, set_])
    return data


def place_bet(driver, urls, bet, kf, textvariable):
    count_bet = 0
    chekpoint = ['test']
    for url in urls:
        try:
            player = []
            number_1 = url.split('https://1xstavka.ru/en/live/Tennis/')[1].split('/')[0]
            number_main = url.split(f"{number_1}" + '/')[1].split('-')[0]
            driver.get(url)
            time.sleep(2)

            one_name = driver.find_element_by_xpath(
                f'//*[@id="{number_main}"]/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]/span').text
            two_name = driver.find_element_by_xpath(
                f'//*[@id="{number_main}"]/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[2]/td[1]/span').text

            data_player = read_analitics_file()

            driver.find_element_by_class_name('scoreboard-nav__select').click()
            time.sleep(2)
            set_ = driver.find_element_by_xpath(
                f'//*[@id="{int(number_main)}"]/div[1]/div[3]/div/div[1]/div[1]/div/div[3]/ul/li[2]')
            set_text = set_.text
            set_.click()
            time.sleep(4)

            player.append([f"{one_name}", f"{two_name}", f"{set_text}"])

            if player[0] in data_player:
                logger.info('-- Game Detected --')



            else:
                # Достаем все элементы div
                divs = driver.find_elements_by_tag_name('div')

                # чекпоинт для нахождения нужного блока
                cheackpoint = 0


                for div in divs:
                    try:
                        # В блоках ищем наши ставки
                        if div.get_attribute('class') == 'bets betCols2':
                            divs_in_div = div.find_elements_by_tag_name('div')
                            for div_span in divs_in_div:
                                n = 0
                                span_list = div_span.find_elements_by_tag_name('span')

                                for span in span_list:
                                    # поиск нужного блока со ставкой
                                    if span.text == textvariable or span.text == textvariable:
                                        cheackpoint += 1

                                    if cheackpoint == 1:
                                        n += 1


                                    if n == 2:
                                        koef = span.text
                                        koef = float(koef)
                                        kf = float(kf)

                                        if koef >= kf:
                                            if chekpoint[0] == textvariable or chekpoint[0] == textvariable:
                                                span.click()
                                                try:
                                                    with open('analytics_file.txt', 'a') as filename:
                                                        filename.write(f'{one_name} | {two_name} | {bet[count_bet]} | {set_text}' + '\n')
                                                        count_bet += 1
                                                        filename.close()
                                                        logger.debug('Save [analytics_file]')
                                                        break
                                                except Exception as e:
                                                    pass

                                    chekpoint[0] = span.text

                    except Exception as e:
                        pass


            time.sleep(5)

        except Exception as e:
            pass
