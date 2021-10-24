import requests
import json
from bs4 import BeautifulSoup
import datetime
import time

# GLOBAL VARIABLE
SAVE_API_URL = 'http://localhost:9090/api/base_rate'
SAVE_API_HEADERS = {
    'Content-Type': 'application/json',
    'api_token': 'Pvk4coiwHqt3ZqQ8SfJD!'
}
CRAWLING_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
}
TARGET_CRAWLING_SETTING = {
    'us': {
        'name': 'KR_NAVER',
        'url': 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%AF%B8%EA%B5%AD+%EC%A4%91%EC%95%99%EC%9D%80%ED%96%89+%EA%B8%B0%EC%A4%80%EA%B8%88%EB%A6%AC&oquery=%EB%AF%B8%EA%B5%AD+%EA%B8%B0%EC%A4%80%EA%B8%88%EB%A6%AC&tqi=hTW%2B0lp0JywssT7mfvwssssstkN-089736',
        'from': 'NAVER',
        'code': 'US'
    },
    'cn': {
        'name': 'CN_NAVER',
        'url': 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%A4%91%EA%B5%AD+%EC%A4%91%EC%95%99+%EC%9D%80%ED%96%89+%EA%B8%B0%EC%A4%80%EA%B8%88%EB%A6%AC',
        'from': 'NAVER',
        'code': 'CN'
    },
    'kr': {
        'name': 'US_NAVER',
        'url': 'https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=%ED%95%9C%EA%B5%AD+%EC%9D%80%ED%96%89+%EA%B8%B0%EC%A3%BC&qdt=0&ie=utf8&query=%ED%95%9C%EA%B5%AD%EC%9D%80%ED%96%89+%EA%B8%B0%EC%A4%80%EA%B8%88%EB%A6%AC',
        'from': 'NAVER',
        'code': 'KR'
    }
}


def save_data(request_body):
    save_response = requests.post(url=SAVE_API_URL, headers=SAVE_API_HEADERS, data=json.dumps(request_body))
    if save_response.status_code == 200:
        return True
    else:
        return False


def make_request_body(counrty_code, rate, from_data, timestamp):
    return {
        "countryCode": counrty_code,
        "rate": rate,
        "fromData": from_data,
        "timestamp": timestamp
    }


def get_korea_naver_search_crawling():
    raw_crawling = requests.get(url=TARGET_CRAWLING_SETTING['kr']['url'], headers=CRAWLING_HEADERS)
    if raw_crawling.status_code == 200:
        html = raw_crawling.text
        soup = BeautifulSoup(html, 'html.parser')
        base_rate_str = soup.select_one('#main_pack > div.sc_new.cs_common_module.case_list.color_1._CPI > div.cm_content_wrap > div:nth-of-type(1) > div > div > div > div.top_info > strong').text
        base_rate = float(base_rate_str.replace('%', ''))
        return [base_rate, int(datetime.datetime.now().timestamp())]
    else:
        return []


def get_china_naver_search_crawling():
    raw_crawling = requests.get(url=TARGET_CRAWLING_SETTING['cn']['url'], headers=CRAWLING_HEADERS)
    if raw_crawling.status_code == 200:
        html = raw_crawling.text
        soup = BeautifulSoup(html, 'html.parser')
        base_rate_str = soup.select_one('#main_pack > div.sc_new.cs_common_module.case_list.color_1._CPI > div.cm_content_wrap > div:nth-of-type(1) > div > div > div > div.top_info > strong').text
        base_rate = float(base_rate_str.replace('%', ''))
        return [base_rate, int(datetime.datetime.now().timestamp())]
    else:
        return []


def get_usa_naver_search_crawling():
    raw_crawling = requests.get(url=TARGET_CRAWLING_SETTING['us']['url'], headers=CRAWLING_HEADERS)
    if raw_crawling.status_code == 200:
        html = raw_crawling.text
        soup = BeautifulSoup(html, 'html.parser')
        base_rate_str = soup.select_one(
            '#main_pack > div.sc_new.cs_common_module.case_list.color_1._CPI > div.cm_content_wrap > div:nth-of-type(1) > div > div > div > div.top_info > strong'
        ).text
        base_rate = float(base_rate_str.replace('%', ''))
        return [base_rate, int(datetime.datetime.now().timestamp())]
    else:
        return []


def main(args):
    final_return_value = {
        'payload': 'get_base_rate'
    }

    kr_name = TARGET_CRAWLING_SETTING['kr']['name']
    kr_code = TARGET_CRAWLING_SETTING['kr']['code']
    kr_from = TARGET_CRAWLING_SETTING['kr']['from']
    kr_data = get_korea_naver_search_crawling()
    if len(kr_data) > 0:
        kr_request_body = make_request_body(kr_code, kr_data[0], kr_from, kr_data[1])
        if save_data(kr_request_body):
            final_return_value[kr_name]= 'success'
        else:
            final_return_value[kr_name] = 'save error'
    else:
        final_return_value[kr_name] = 'call error'

    time.sleep(1)

    us_name = TARGET_CRAWLING_SETTING['us']['name']
    us_code = TARGET_CRAWLING_SETTING['us']['code']
    us_from = TARGET_CRAWLING_SETTING['us']['from']
    us_data = get_usa_naver_search_crawling()
    if len(us_data) > 0:
        us_request_body = make_request_body(us_code, us_data[0], us_from, us_data[1])
        if save_data(us_request_body):
            final_return_value[us_name] = 'success'
        else:
            final_return_value[us_name] = 'save error'
    else:
        final_return_value[us_name] = 'call error'

    time.sleep(1)

    cn_name = TARGET_CRAWLING_SETTING['cn']['name']
    cn_code = TARGET_CRAWLING_SETTING['cn']['code']
    cn_from = TARGET_CRAWLING_SETTING['cn']['from']
    cn_data = get_china_naver_search_crawling()
    if len(cn_data) > 0:
        cn_request_body = make_request_body(cn_code, cn_data[0], cn_from, cn_data[1])
        if save_data(cn_request_body):
            final_return_value[cn_name] = 'success'
        else:
            final_return_value[cn_name] = 'save error'
    else:
        final_return_value[cn_name] = 'call error'
    return final_return_value


print(main(0))
