import requests
import json
from bs4 import BeautifulSoup
import datetime
import time

def save_data(request_body):
    url = "http://finance.godpark.pe.kr/api/base_rate"
    headers = {
        'Content-Type': 'application/json',
        'api_token': 'Pvk4coiwHqt3ZqQ8SfJD!'
    }
    save_response = requests.post(url=url, headers=headers, data=json.dumps(request_body))
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
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=%ED%95%9C%EA%B5%AD+%EC%9D%80%ED%96%89+%EA%B8%B0%EC%A3%BC&qdt=0&ie=utf8&query=%ED%95%9C%EA%B5%AD%EC%9D%80%ED%96%89+%EA%B8%B0%EC%A4%80%EA%B8%88%EB%A6%AC"
    headers = {
        'User-Agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
    }
    raw_crawling = requests.get(url=url, headers=headers)
    if raw_crawling.status_code == 200:
        html = raw_crawling.text
        soup = BeautifulSoup(html, 'html.parser')
        base_rate_str = soup.select_one('#main_pack > div.sc_new.cs_common_module.case_list.color_1._CPI > div.cm_content_wrap > div:nth-of-type(1) > div > div > div > div.top_info > strong').text
        base_rate = float(base_rate_str.replace('%', ''))
        return True, 'KR', base_rate, int(datetime.datetime.now().timestamp())
    else:
        return False, 'KR', 0, 0


def get_china_naver_search_crawling():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%A4%91%EA%B5%AD+%EC%A4%91%EC%95%99+%EC%9D%80%ED%96%89+%EA%B8%B0%EC%A4%80%EA%B8%88%EB%A6%AC'
    headers = {
        'User-Agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
    }
    raw_crawling = requests.get(url=url, headers=headers)
    if raw_crawling.status_code == 200:
        html = raw_crawling.text
        soup = BeautifulSoup(html, 'html.parser')
        base_rate_str = soup.select_one('#main_pack > div.sc_new.cs_common_module.case_list.color_1._CPI > div.cm_content_wrap > div:nth-of-type(1) > div > div > div > div.top_info > strong').text
        base_rate = float(base_rate_str.replace('%', ''))
        return True, 'CN', base_rate, int(datetime.datetime.now().timestamp())
    else:
        return False, 'CN', 0, 0


def get_usa_naver_search_crawling():
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%AF%B8%EA%B5%AD+%EC%A4%91%EC%95%99%EC%9D%80%ED%96%89+%EA%B8%B0%EC%A4%80%EA%B8%88%EB%A6%AC&oquery=%EB%AF%B8%EA%B5%AD+%EA%B8%B0%EC%A4%80%EA%B8%88%EB%A6%AC&tqi=hTW%2B0lp0JywssT7mfvwssssstkN-089736'
    headers = {
        'User-Agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
    }
    raw_crawling = requests.get(url=url, headers=headers)
    if raw_crawling.status_code == 200:
        html = raw_crawling.text
        soup = BeautifulSoup(html, 'html.parser')
        base_rate_str = soup.select_one(
            '#main_pack > div.sc_new.cs_common_module.case_list.color_1._CPI > div.cm_content_wrap > div:nth-of-type(1) > div > div > div > div.top_info > strong'
        ).text
        base_rate = float(base_rate_str.replace('%', ''))
        return True, 'US', base_rate, int(datetime.datetime.now().timestamp())
    else:
        return False, 'US', 0, 0

def main():
    final_return_value = {
        'payload': 'get_base_rate'
    }
    kr_check_status, kr_country_code, kr_base_rate, kr_timestamp = get_korea_naver_search_crawling()
    if kr_check_status:
        kr_request_body = make_request_body(kr_country_code, kr_base_rate, 'NAVER', kr_timestamp)
        if save_data(kr_request_body):
            final_return_value['KR_NAVER']= 'success'
        else:
            final_return_value['KR_NAVER'] = 'save error'
    else:
        final_return_value['KR_NAVER'] = 'call error'

    time.sleep(1)

    us_check_status, us_country_code, us_base_rate, us_timestamp = get_usa_naver_search_crawling()
    if us_check_status:
        us_request_body = make_request_body(us_country_code, us_base_rate, 'NAVER', us_timestamp)
        if save_data(us_request_body):
            final_return_value['US_NAVER'] = 'success'
        else:
            final_return_value['US_NAVER'] = 'save error'
    else:
        final_return_value['US_NAVER'] = 'call error'
    return final_return_value

    time.sleep(1)

    cn_check_status, cn_country_code, cn_base_rate, cn_timestamp = get_china_naver_search_crawling()
    if cn_check_status:
        us_request_body = make_request_body(cn_country_code, cn_base_rate, 'NAVER', cn_timestamp)
        if save_data(us_request_body):
            final_return_value['CN_NAVER'] = 'success'
        else:
            final_return_value['CN_NAVER'] = 'save error'
    else:
        final_return_value['CN_NAVER'] = 'call error'
    return final_return_value

print(main())
