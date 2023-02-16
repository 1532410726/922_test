import pytest
import requests

from L1.log_utils import logger


class TestPetstorePet:
    '''
    宠物商店宠物查询接口
    '''

    def setup_class(self):
        # 定义请求url
        self.base_url = "https://petstore.swagger.io/v2/pet"
        # 拼接查询接口
        self.search_url = self.base_url + "/findByStatus"

    # 正常查询
    @pytest.mark.parametrize("status", ["available", "pending"],
                             ids=["available_pets", "pending_pets"])
    def test_search_pet(self, status):
        pet_status = {
            "status": status
        }
        r = requests.get(self.search_url, params=pet_status)
        # 打印log
        logger.info(r.status_code)
        assert r.status_code == 200
        assert r.json() != []
        assert "id" in r.json()[0]

    # 输出异常查询
    @pytest.mark.parametrize("status", ["petstatus", "123456", "", "sold"])
    def test_search_pet_failure(self, status):
        pet_status = {
            "status": status
        }
        r = requests.get(self.search_url, params=pet_status)
        # 打印log
        logger.info(r.status_code)
        assert r.status_code == 200
        # assert r.json() == []

    # 不传status参数
    def test_est_search_pet_null(self):
        r = requests.get(self.search_url)
        logger.info(r.status_code)
        assert r.status_code == 200
        assert r.json() == []

    # 传入非status参数
    def test_search_pet_wrong(self):
        pet_status = {
            "key": "value"
        }
        r = requests.get(self.search_url, params=pet_status)
        logger.info(r.status_code)
        assert r.status_code == 200
        assert r.json() == []
