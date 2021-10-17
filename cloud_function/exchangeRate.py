import requests
import json
from bs4 import BeautifulSoup
import datetime

def save_data(request_body):
    url = "http://localhost:9090/api/exchange_rate"
    headers = {
        'Content-Type': 'application/json',
        'api_token': 'Pvk4coiwHqt3ZqQ8SfJD!'
    }
    save_response = requests.post(url=url, headers=headers, data=json.dumps(request_body))
    if save_response.status_code == 200:
        return True
    else:
        return False


def make_request_body(currency_code, currency_price, from_data, timestamp):
    return {
        "currencyCode": currency_code,
        "currencyPrice": currency_price,
        "fromData": from_data,
        "timestamp": timestamp
    }

def get_exchange_freeforex_api():
    url = "https://www.freeforexapi.com/api/live?pairs=USDKRW"
    get_response = requests.get(url=url)
    if get_response.status_code == 200:
        result_data = get_response.json()
        if result_data['code'] != 200:
            return False, 'USD', 0, 0
        if result_data['rates'] and result_data['rates']['USDKRW']:
            return True, 'USD', result_data['rates']['USDKRW']['rate'], result_data['rates']['USDKRW']['timestamp']
    else:
        return False, 'USD', 0, 0

def get_exchange_investing_crawling():
    url = "https://kr.investing.com/currencies/usd-krw"
    headers = {
        'User-Agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
    }
    raw_crawling = requests.get(url=url, headers=headers)
    if raw_crawling.status_code == 200:
        html = raw_crawling.text
        soup = BeautifulSoup(html, 'html.parser')
        currency_price = soup.select_one('#last_last').text.replace(',', '')
        return True, 'USD', float(currency_price), int(datetime.datetime.now().timestamp())
    else:
        return False, 'USD', 0, 0



def main():
    final_return_value = {
        'payload': 'get_exchange_data'
    }

    freefore_check_status, freefore_currency_code, freefore_currency_price, freefore_timestamp = get_exchange_freeforex_api()
    if freefore_check_status:
        freefore_request_body = make_request_body(freefore_currency_code, freefore_currency_price, 'FREEFOREX', freefore_timestamp)
        if save_data(freefore_request_body):
            final_return_value['FREEFOREX'] = 'success'
        else:
            final_return_value['FREEFOREX'] = 'save error'
    else:
        final_return_value['FREEFOREX'] = 'call error'

    investing_check_status, investing_currency_code, investing_currency_price, investing_timestamp = get_exchange_investing_crawling()
    if investing_check_status:
        investing_request_body = make_request_body(investing_currency_code, investing_currency_price, 'INVESTING', investing_timestamp)
        if save_data(investing_request_body):
            final_return_value['INVESTING'] = 'success'
        else:
            final_return_value['INVESTING'] = 'save error'
    else:
        final_return_value['INVESTING'] = 'call error'

    return final_return_value

print(main())