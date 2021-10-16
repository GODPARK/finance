import requests
import json


def save_data(request_body):
    url = "http://localhost:9090/api/exchange_rate"
    headers = {
        'Content-Type': 'application/json',
        'api_token': 'Pvk4coiwHqt3ZqQ8SfJD!'
    }
    save_response = requests.post(url=url, headers=headers, data=json.dumps(request_body))
    if save_response.status_code == 200:
        print(save_response.text)
    else:
        print('save error')


def make_request_body(currency_code, currency_price, from_data, timestamp):
    return {
        "currencyCode": currency_code,
        "currencyPrice": currency_price,
        "fromData": from_data,
        "timestamp": timestamp
    }

def get_exchange_freeforexapi():
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


def main():
    freefore_check_status, freefore_currency_code, freefore_currency_price, freefore_timestamp = get_exchange_freeforexapi()
    if freefore_check_status:
        freefore_request_body = make_request_body(freefore_currency_code, freefore_currency_price, 'FREEFOREX', freefore_timestamp)
        save_data(freefore_request_body)

main()