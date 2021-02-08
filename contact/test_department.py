import pytest

from contact.my_token import WeiChat
import requests
import logging
import json

class TestDepartment:
    logging.basicConfig(level=logging.DEBUG)
    @classmethod
    def setup_class(cls):
        WeiChat.get_token()
        print(WeiChat._token)

    def setup(self):
        print("setup")

    # 创建多层级部门
    def test_creat_depth(self):
        parentid = 1
        for i in range(5):
            data = {"name": "广州研发中心"+parentid,
                    "parentid": parentid,
                    }
            r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": WeiChat.get_token()},
                          json=data
                          ).json()  # params和json的区别？
            logging.debug(r)
            parentid = r["id"]
            assert r["errcode"] == 0

        # 对name等进行参数化测试

    @pytest.mark.parametrize("name", [
        "广州研发中心",
        "東京アニメ研究所",
        "도쿄 애니메이션 연구소"
        ])
    def test_creat_name(self, name):
        data = {"name": name, "name_en": "RDGZ", "parentid": 1, "order": 1, "id": 2}
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": WeiChat.get_token()},
                          json=data
                          ).json()  # params和json的区别？
        logging.debug(r)

    def test_creat_order(self):
        data = {"name": "广州研发中心", "name_en": "RDGZ", "parentid": 1, "order": 1, "id": 2}
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                          params={"access_token": WeiChat.get_token()},
                          json=data
                          ).json()  # params和json的区别？
        logging.debug(r)
        assert r["errcode"] == 0

    def test_get(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token=ACCESS_TOKEN&id=ID",
                     params={"access_token": WeiChat.get_token()},
                     ).json()
        logging.debug(json.dumps(r, indent=2))  # 格式化输出

    # 加密解密 requests-hook