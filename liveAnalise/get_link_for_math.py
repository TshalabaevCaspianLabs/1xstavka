from loguru import logger


def get_link_math(driver):
    scores_total_low = [
        ['4', '2'],
        ['4', '1'],
        ['5', '3'],
        ['5', '2'],
        ['2', '4'],
        ['1', '4'],
        ['3', '5'],
        ['2', '5']
    ]
    driver.get('https://1xstavka.ru/live/Tennis/')
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

                        except:
                            pass
                    if len(score_player) == 2:
                        if score_player in scores_total_low:
                            logger.debug(score_player)
                            url_with_site = div.find_element_by_class_name('c-events__name').get_attribute('href')
                            url_game.append(url_with_site)

        except:
            pass

    return url_game
