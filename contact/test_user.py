import requests
from contact.my_token import WeiChat
import time
import logging
import pystache

class TestUser():
    logging.basicConfig(level=logging.DEBUG)
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

    def test_creat_by_template(self):
        print(pystache.render("hello {{name}} {{#has}} world {{value}} {{/has}}",
                              {"name": "hogwarts", "has": True, "value": "test"}))

    def test_list(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                         params={"access_token": WeiChat.get_token(), "department_id": 1},
                         ).json()
        logging.debug(r)

    def get_user(self, dict):
        template = "".join(open("user_creat.json").readlines())
        logging.debug(template)

        return pystache.render(template, dict)