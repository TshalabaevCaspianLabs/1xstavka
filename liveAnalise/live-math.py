import json
import time

import requests
from loguru import logger


def math():
    logger.error('\n[--] Только те где есть активный счет!\n')

    url = 'https://1xstavka.ru/LiveFeed/Get1x2_VZip?sports=4&count=50&antisports=188&mode=4&country=1&partner=51&getEmpty=true&noFilterBlockEvent=true'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    cookies = {
        'lng': 'ru',
        'flaglng': 'ru',
        'typeBetNames': 'short',
        'auid': 'WNT5hGBDTDJ2tTKIIZuzAg==',
        'right_side': 'right',
        '_ym_uid': "1615023161827510060",
        '_ym_d': "1615023161",
        '_ga': 'GA1.2.120794411.1615023163',
        'sh.session_be98639c': 'a15cc309-2c69-447b-895d-e0048768c817',
        'SESSION': '563e848043a3323d15a992fe97e2de12',
        'dnb': "1",
        'visit': '1-d9d98026d8284dd55bb1321a36b65fe9',
        'coefview': "0",
        'tzo': '5',
        'blocks': '1%2C1%2C1%2C1%2C1%2C1%2C1%2C1',
        'completed_user_settings': 'true',
        '_glhf': '1615592690',
        '_ym_visorc': 'w',
        'ggru': '153',
        '_gid': 'GA1.2.659311275.1615574923',
        '_ym_isad': '1'
    }
    html = requests.get(url, headers=headers, cookies=cookies)
    data = json.loads(html.text)

    for dt in data['Value']:
        data_for_url = []
        try:
            if len(dt['SC']['PS']) == 3:
                try:
                    scope_one = dt['SC']['PS'][2]['Value']['S1']
                    one = dt['O1']

                    scope_two = dt['SC']['PS'][2]['Value']['S2']
                    two = dt['O2']

                    if one > two or one < two:
                        data_for_url.append(dt)

                    logger.opt(ansi=True).warning(
                        f'{one} | <red>[{scope_one}]</red> -- {two} | <red>[{scope_two}]</red>')
                except:
                    try:
                        scope_one = dt['SC']['PS'][2]['Value']['S1']
                        one = dt['O1']
                        two = dt['O2']
                        if one > two or one < two:
                            data_for_url.append(dt)
                        logger.opt(ansi=True).warning(f'{one} | <red>[{scope_one}]</red> -- {two} | <red>[{0}]</red>')

                    except:
                        one = dt['O1']
                        scope_two = dt['SC']['PS'][2]['Value']['S2']
                        two = dt['O2']
                        if one > two or one < two:
                            data_for_url.append(dt)
                        logger.opt(ansi=True).warning(f'{one} | <red>[{0}]</red> -- {two} | <red>[{scope_two}]</red>')



            else:

                if len(dt['SC']['PS']) == 2:
                    try:
                        scope_one = dt['SC']['PS'][1]['Value']['S1']
                        one = dt['O1']

                        scope_two = dt['SC']['PS'][1]['Value']['S2']
                        two = dt['O2']
                        if one > two or one < two:
                            data_for_url.append(dt)
                        logger.opt(ansi=True).warning(
                            f'{one} | <red>[{scope_one}]</red> -- {two} | <red>[{scope_two}]</red>')

                    except:
                        try:
                            scope_one = dt['SC']['PS'][1]['Value']['S1']
                            one = dt['O1']

                            two = dt['O2']
                            if one > two or one < two:
                                data_for_url.append(dt)
                            logger.opt(ansi=True).warning(
                                f'{one} | <red>[{scope_one}]</red> -- {two} | <red>[{0}]</red>')

                        except:
                            one = dt['O1']

                            scope_two = dt['SC']['PS'][1]['Value']['S2']
                            two = dt['O2']
                            if one > two or one < two:
                                data_for_url.append(dt)
                            logger.opt(ansi=True).warning(
                                f'{one} | <red>[{0}]</red> -- {two} | <red>[{scope_two}]</red>')

                else:

                    if len(dt['SC']['PS']) == 1:

                        try:
                            scope_one = dt['SC']['PS'][0]['Value']['S1']
                            one = dt['O1']

                            scope_two = dt['SC']['PS'][0]['Value']['S2']
                            two = dt['O2']
                            if one > two or one < two:
                                data_for_url.append(dt)
                            logger.opt(ansi=True).warning(
                                f'{one} | <red>[{scope_one}]</red> -- {two} | <red>[{scope_two}]</red>')

                        except:
                            try:
                                scope_one = dt['SC']['PS'][0]['Value']['S1']
                                one = dt['O1']

                                two = dt['O2']
                                if one > two or one < two:
                                    data_for_url.append(dt)
                                logger.opt(ansi=True).warning(
                                    f'{one} | <red>[{scope_one}]</red> -- {two} | <red>[{0}]</red>')

                            except:
                                one = dt['O1']

                                scope_two = dt['SC']['PS'][2]['Value']['S2']
                                two = dt['O2']
                                if one > two or one < two:
                                    data_for_url.append(dt)
                                logger.opt(ansi=True).warning(
                                    f'{one} | <red>[{0}]</red> -- {two} | <red>[{scope_two}]</red>')

        except Exception as e:
            pass
    logger.error('\n------------------------------------------------------------\n\n\n\n\n')


if __name__ == '__main__':
    while True:
        math()
        time.sleep(5)
