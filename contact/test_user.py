import requests
from contact.my_token import WeiChat
import time
import logging
import pystache

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug("test")


class TestUser():

    depart_id = 1
    @classmethod
    def setup_class(cls):
        # 创建部门
        pass

    def test_creat(self):
        uid = str(time.time())
        data = {
            "userid": uid,
            "name": uid,
            "department": [self.depart_id],
            "email": uid+"@testerhome.com"
        }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN",
                          params=WeiChat.get_token(),
                          json=data
                          ).json()
        assert r["errcode"] == 0

    def test_creat_by_template(self):
        uid = "test" + str(time.time())
        mobile = str(time.time()).replace(".", "")[0:11]
        data = self.get_user(self.get_user({
            "name": uid,
            "title": "tester",
            "mail": "cyliu@163.com",
            "mobile": mobile,

        }))
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN",
                          params=WeiChat.get_token(),
                          data=data,
                          headers={"content-type": "application/json"}
                          ).json()
        assert r["errcode"] == 0

    def test_list(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                         params={"access_token": WeiChat.get_token(), "department_id": 1},
                         ).json()
        logging.debug(r)

    def get_user(self, dict):
        logging.basicConfig(level=logging.DEBUG)
        template = "".join(open("user_creat_file.json", encoding='utf-8').readlines())
        logger.debug(template)
        return pystache.render(template, dict)

    def test_get_user(self):
        logger.debug(self.get_user({"name": "test", "title": "tester", "mail": "cyliu@163.com"}))
