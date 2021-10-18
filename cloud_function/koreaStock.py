import requests
import json
from bs4 import BeautifulSoup
import datetime
import time

def save_data(request_body):
    url = "http://localhost:9090/api/korea_stock"
    headers = {
        'Content-Type': 'application/json',
        'api_token': 'Pvk4coiwHqt3ZqQ8SfJD!'
    }
    save_response = requests.post(url=url, headers=headers, data=json.dumps(request_body))
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
    url = "https://kr.investing.com/indices/kospi-chart"
    headers = {
        'User-Agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
    }
    raw_crawling = requests.get(url=url, headers=headers)
    if raw_crawling.status_code == 200:
        html = raw_crawling.text
        soup = BeautifulSoup(html, 'html.parser')
        kospi_str = soup.select_one(
            '#last_last'
        ).text
        kospi_number = float(kospi_str.replace(",", ''))
        return True, 'KOSPI', kospi_number, int(datetime.datetime.now().timestamp())
    else:
        return False, 'KOSPI', 0, 0


def get_samsung_google_crawling():
    url = "https://www.google.com/finance/quote/005930:KRX"
    headers = {
        'User-Agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
    }
    raw_crawling = requests.get(url=url, headers=headers)
    if raw_crawling.status_code == 200:
        html = raw_crawling.text
        soup = BeautifulSoup(html, 'html.parser')
        samsung_str = soup.find_all('div', 'YMlKec fxKbKc')[0].text
        samsung_number = float(samsung_str.replace(",", '').replace("₩", ''))
        return True, 'SAMSUNG', samsung_number, int(datetime.datetime.now().timestamp())
        return
    else:
        return False, 'SAMSUNG', 0, 0

def main():
    final_return_value = {
        'payload': 'get_korea_stock'
    }
    kospi_check_status, kospi_code, kospi_price, kospi_timestamp = get_kospi_investing_crawling()
    if kospi_check_status:
        kospi_request_body = make_request_body(kospi_code, kospi_price, 'INVESTING', kospi_timestamp)
        if save_data(kospi_request_body):
            final_return_value['KOSPI'] = 'success'
        else:
            final_return_value['KOSPI'] = 'save error'
    else:
        final_return_value['KOSPI'] = 'call error'

    samsung_check_status, samsung_code, samsung_price, samsung_timestamp = get_samsung_google_crawling()
    if samsung_check_status:
        samsung_request_body = make_request_body(samsung_code, samsung_price, 'GOOGLE', samsung_timestamp)
        if save_data(samsung_request_body):
            final_return_value['SAMSUNG'] = 'success'
        else:
            final_return_value['SAMSUNG'] = 'save error'
    else:
        final_return_value['SAMSUNG'] = 'call error'

    return final_return_value


print(main())