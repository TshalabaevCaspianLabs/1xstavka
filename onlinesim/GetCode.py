import json

import requests
from loguru import logger as log
import time

def getLastCode():
    url = 'https://onlinesim.ru/api/rent/getRentState.php?apikey=a365dd4e3b9ccf932e9172e3ae2f2a4b'
    proxies = {
        'http': 'http://Seltima05ta58:E4n1DjG@185.33.85.92:45785',
        'https': 'https://Seltima05ta58:E4n1DjG@185.33.85.92:45785'
    }
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    html = requests.get(url, headers=headers, proxies=proxies)
    data = json.loads(html.text)
    code = data['list'][0]['messages']['data'][0][0]['code']
    return code


def getNewCode(lastcode):
    url = 'https://onlinesim.ru/api/rent/getRentState.php?apikey=a365dd4e3b9ccf932e9172e3ae2f2a4b'
    proxies = {
        'http': 'http://Seltima05ta58:E4n1DjG@185.33.85.92:45785',
        'https': 'https://Seltima05ta58:E4n1DjG@185.33.85.92:45785'
    }
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    while True:
        html = requests.get(url, headers=headers, proxies=proxies)
        data = json.loads(html.text)
        code = data['list'][0]['messages']['data'][0][0]['code']

        if code != lastcode:
            log.debug(f'Code accepted -- [{code}]')
            return code
            break

        else:
            log.error('Not Code')
            time.sleep(2)




