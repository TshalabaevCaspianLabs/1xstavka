from loguru import logger


def get_total_low():
    data = []
    with open('/Users/macbookpro/Documents/1xstavka/liveAnalise/algoritm_bet.txt', 'r') as file:
        for bet in file:
            bet = bet.strip()
            one, two = bet.split(":")
            data.append([f'{one}', f'{two}'])

    return data


def get_link_math(driver):
    scores_total_low = get_total_low()
    driver.get('https://1xstavka.ru/en/live/Tennis/')
    url_game = []
    div_list = driver.find_elements_by_tag_name('div')
    for div in div_list:
        try:
            score_player = []
            if div.get_attribute('class') == 'c-events-scoreboard__layout':
                SET_NOW = div.find_element_by_class_name('c-events__overtime')
                scores = div.find_elements_by_class_name('c-events-scoreboard__line')
                for score in scores:
                    span_list = score.find_elements_by_tag_name('span')
                    for span in span_list:
                        try:
                            if span.get_attribute('title') == f'{SET_NOW.text}':
                                score_ = span.text
                                score_player.append(score_)

                        except Exception as e:
                            pass
                    if len(score_player) == 2:
                        if score_player in scores_total_low:
                            logger.debug(score_player)
                            url_with_site = div.find_element_by_class_name('c-events__name').get_attribute('href')
                            url_game.append(url_with_site)

        except Exception as e:
            pass

    return url_game
