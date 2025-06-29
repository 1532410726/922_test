import sys
import os
# 将项目根目录添加到 sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import pytest
import requests
from L1.log_utils import logger


@pytest.fixture(scope="module")
def token():
    """获取token的fixture，整个模块只执行一次"""
    url = "https://apitest.dingdingclub.com/sv-invest/login/userLogin"
    body = {
        "login": "lipeifeng", "code": "", "password": "123456"
    }
    r = requests.post(url, json=body)
    response_data = r.json()
    token = response_data["data"]["token"]
    assert r.status_code == 200
    assert response_data["message"] == "OK!"
    return token


class TestShortPlay:
    def test_get_account(self, token):
        """获取快手账号"""
        url = "https://apitest.dingdingclub.com/sv-invest/kuaishou/baseData/getAccount"
        headers = {
            'Authorization': f"{token}",
            'Content-Type': 'application/json',
            '__auth_app_name__': 'sv-invest'
        }
        r = requests.post(url, headers=headers, json={})
        account_data = r.json()
        assert r.status_code == 200
        assert account_data["message"] == "OK!"
    @pytest.mark.parametrize(
        "body", [
            {
                "pageNo": 1,
                "pageSize": 10,
                "selfSetFootPosition": "true",
                "ivtUserId": "24",
                "startDate": "2024-12-24",
                "endDate": "2025-01-22"
            },
            {
                "pageNo": 1,
                "pageSize": 10,
                "selfSetFootPosition": "true",
                "ivtUserId": "24"
            }
        ]
    )
    def test_get_account_list(self, token, body):
        """获取快手媒体账户统计列表"""
        url = "https://apitest.dingdingclub.com/sv-invest/kuaishou/accountList"
        headers = {
            'Authorization': f"{token}",
            'Content-Type': 'application/json',
            '__auth_app_name__': 'sv-invest'
        }
        r = requests.post(url, headers=headers, json=body)
        account_data = r.json()
        assert r.status_code == 200
        assert account_data["message"] == "OK!"
