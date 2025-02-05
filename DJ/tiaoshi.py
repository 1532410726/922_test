import json

import pytest
import requests


def get_account():
    url = "https://apitest.dingdingclub.com/sv-invest/kuaishou/baseData/getAccount"
    token = "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJmNDg2ZTNjZjc4MWQ0ODIzOGJmNGI2ZjIzNmZkNDA3OSIsInVuYW1lIjoi5p2O5rKb5bOwIiwibmlja05hbWUiOiIiLCJwaG9uZSI6IiIsImVtYWlsIjoiIiwic3ViIjoiMjQifQ.1WB0gZHhGUQMAwnbJl_GIB9S1tBpYx3dEhQh3Ngcu-w1YyVJDbfhcPy1vgwXHnh0Qkt4ZFPYsizG9XwwIEGFqA"
    headers = {
        'Authorization': f"{token}",
        'Content-Type': 'application/json',  # 其他常用头部设置
        '__auth_app_name__': 'sv-invest'
    }
    r = requests.post(url, headers=headers, json={})
    # account_data = r.json()
    assert r.status_code == 200
    print(r.text)
    # assert account_data["message"] == "OK!"


if __name__ == '__main__':
    get_account()
