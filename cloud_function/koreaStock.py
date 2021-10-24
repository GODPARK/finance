import requests
import json
from bs4 import BeautifulSoup
import datetime

# GLOBAL VARIABLE
SAVE_API_URL = 'http://localhost:9090/api/korea_stock'
SAVE_API_HEADERS = {
    'Content-Type': 'application/json',
    'api_token': 'Pvk4coiwHqt3ZqQ8SfJD!'
}
CRAWLING_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
}
TARGET_CRAWLING_SETTING = {
    'kospi': {
        'name': 'KOSPI',
        'url': 'https://kr.investing.com/indices/kospi-chart',
        'from': 'INVESTING'
    },
    'samsung': {
        'name': 'SAMSUNG',
        'url': 'https://www.google.com/finance/quote/005930:KRX',
        'from': 'GOOGLE'
    }
}


def save_data(request_body):
    save_response = requests.post(url=SAVE_API_URL, headers=SAVE_API_HEADERS, data=json.dumps(request_body))
    if save_response.status_code == 200:
        return True
    else:
        return False


def make_request_body(stock_code, stock_price, from_data, timestamp):
    return {
        "stockCode": stock_code,
        "stockPrice": stock_price,
        "fromData": from_data,
        "timestamp": timestamp
    }


def get_kospi_investing_crawling():
    raw_crawling = requests.get(url=TARGET_CRAWLING_SETTING['kospi']['url'], headers=CRAWLING_HEADERS)
    if raw_crawling.status_code == 200:
        html = raw_crawling.text
        soup = BeautifulSoup(html, 'html.parser')
        kospi_str = soup.select_one(
            '#last_last'
        ).text
        kospi_number = float(kospi_str.replace(",", ''))
        return [kospi_number, int(datetime.datetime.now().timestamp())]
    else:
        return []


def get_samsung_google_crawling():
    raw_crawling = requests.get(url=TARGET_CRAWLING_SETTING['samsung']['url'], headers=CRAWLING_HEADERS)
    if raw_crawling.status_code == 200:
        html = raw_crawling.text
        soup = BeautifulSoup(html, 'html.parser')
        samsung_str = soup.find_all('div', 'YMlKec fxKbKc')[0].text
        samsung_number = float(samsung_str.replace(",", '').replace("₩", ''))
        return [samsung_number, int(datetime.datetime.now().timestamp())]
        return
    else:
        return []

def main(args):
    final_return_value = {
        'payload': 'get_korea_stock'
    }

    # KOSPI
    kospi_name = TARGET_CRAWLING_SETTING['kospi']['name']
    kospi_data = get_kospi_investing_crawling()
    if len(kospi_data) > 0:
        kospi_request_body = make_request_body(
            kospi_name,
            kospi_data[0],
            TARGET_CRAWLING_SETTING['kospi']['from'],
            kospi_data[1]
        )
        if save_data(kospi_request_body):
            final_return_value[kospi_name] = 'success'
        else:
            final_return_value[kospi_name] = 'save error'
    else:
        final_return_value[kospi_name] = 'call error'

    # SAMSUNG
    samsung_name = TARGET_CRAWLING_SETTING['samsung']['name']
    samsung_data = get_samsung_google_crawling()
    if len(samsung_data) > 0:
        samsung_request_body = make_request_body(
            samsung_name,
            samsung_data[0],
            TARGET_CRAWLING_SETTING['samsung']['from'],
            samsung_data[1]
        )
        if save_data(samsung_request_body):
            final_return_value[samsung_name] = 'success'
        else:
            final_return_value[samsung_name] = 'save error'
    else:
        final_return_value[samsung_name] = 'call error'

    return final_return_value


print(main(0))