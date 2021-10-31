import requests
import json


def save_data(request_body):
    url = "http://localhost:9090/api/cryptocurrency"
    headers = {
        'Content-Type': 'application/json',
        'api_token': 'Pvk4coiwHqt3ZqQ8SfJD!'
    }
    save_response = requests.post(url=url, headers=headers, data=json.dumps(request_body))
    if save_response.status_code == 200:
        return True
    else:
        return False


def make_request_body(crypto_code, min_price, max_price, from_data, timestamp):
    return {
        "cryptoCode": crypto_code,
        "minPrice": min_price,
        "maxPrice": max_price,
        "fromData": from_data,
        "timestamp": timestamp
    }

def get_crypto_currency_price(crypto_code):
    url ="https://api.bithumb.com/public/ticker/" + crypto_code.upper() + "_KRW"
    save_response = requests.get(url=url)
    if save_response.status_code == 200:
        result_data = save_response.json()
        if result_data['data']:
            return True, int(result_data['data']['min_price']), int(result_data['data']['max_price']), int(int(result_data['data']['date'])/1000)
        else:
            return False, 0, 0, 0
    else:
        return False, 0, 0, 0


def main():
    final_return_value = {
        'payload': 'get_cryptocurrency'
    }
    crypto_code_list = ['BTC', 'ETH']

    for crypto_code in crypto_code_list:
        api_result_status, min_price, max_price, timestamp = get_crypto_currency_price(crypto_code)
        if api_result_status and min_price > 0 and max_price > 0:
            api_body = make_request_body(
                crypto_code=crypto_code,
                min_price=min_price,
                max_price=max_price,
                from_data='bithumb',
                timestamp=timestamp
            )
            if save_data(api_body):
                final_return_value[crypto_code] = 'success'
            else:
                final_return_value[crypto_code] = 'fail save api'
        else:
            final_return_value[crypto_code] = 'fail api error'
    return final_return_value


print(main())