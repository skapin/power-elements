# coding: UTF-8
import utils


def test_server_respond_200():
    assert utils.is_status_ok(utils.call('GET', url='/status/is_up').status_code)


def test_server_is_up():
    resp = utils.call('GET', url='/status/is_up')
    server = resp.json()
    assert 'is_up' in server

    assert server.get('is_up')
