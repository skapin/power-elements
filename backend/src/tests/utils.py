# -*- coding: UTF-8 -*-
import datetime
import requests
import pytest


class Settings(object):
    BASE_URL = "http://172.17.0.1:9009"
    DATETIME = '2019-08-28T09:07:57.218Z'
    TEST_CARDS = ['A08020', 'A08021']


def call(method, url, headers=None, **kwargs):
    req_headers = dict()
    if headers:
        req_headers.update(headers)
    return requests.request(method=method, url=Settings.BASE_URL + url, headers=req_headers, **kwargs)


def is_status_ok(status):
    return 200 <= status < 300


def is_iso_date(date):
    try:
        if date:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        pass
    return False


def test_session():
    return Settings.SESSION


def scan_testcard_at(card_n, workstation):

    params = {"code": card_n, "workstation": workstation}
    if card_n < 10 and card_n > 0:
        params['code'] = Settings.TEST_CARDS[card_n]

    return call('POST',
                url='/api/scan_code',
                json=params)


@pytest.fixture
def clean_test_scans():
    call('DELETE',
         url='/api/scans/cards/' + Settings.TEST_CARDS[1]).json()
    call('DELETE',
         url='/api/scans/cards/' + Settings.TEST_CARDS[0]).json()

# @pytest.fixture
# def start_record():
#     return call('POST', url='/record/start', json=Settings.SESSION)


# @pytest.fixture
# def stop_record():
#     return call('POST', url='/record/stop', json={'observator': 'observator_test'})


# @pytest.fixture
# def start_stop_record():
#     yield call('POST', url='/record/start', json=Settings.SESSION)
#     call('POST', url='/record/stop', json={'observator': 'observator_test'})


# def speed_test(method, url, headers=None, iteration=100, **kwargs):
#     total = 0.0
#     nbr = 0.0
#     for x in range(0, iteration):
#         resp = call(method=method, url=url, **kwargs)
#         total += resp.elapsed.total_seconds()
#         nbr += 1
#     print("Speed took: " + str(float(total / nbr)))
#     return float(total / nbr)
