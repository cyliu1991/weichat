
import time
import logging
from contact.user import User
from contact.utils import Utils


class TestUser():

    depart_id = 1
    @classmethod
    def setup_class(cls):
        # 创建部门
        cls.user = User() # user只需要创建一次，放在setup_class中

    def test_creat(self):  # 用例只有数据和逻辑调用
        uid = str(time.time())
        data = {
            "userid": uid,
            "name": uid,
            "department": [self.depart_id],
            "email": uid+"@testerhome.com"
        }
        r = self.user.creat(data)
        assert r["errcode"] == 0

    def test_creat_by_real(self):
        uid = "test" + str(time.time())
        mobile = str(time.time()).replace(".", "")[0:11]
        data = Utils.parse("user_creat_file.json", {
            "name": uid,
            "title": "tester",
            "mail": "cyliu@163.com",
            "mobile": mobile,

        })
        r = self.user.creat(data)
        assert r["errcode"] == 0

    def test_list(self):
        r = self.user.list()
        logging.debug(r)

    def test_get_user(self):
        logging.debug(Utils.parse("user_creat_file.json", {
            "name": "test",
            "title": "tester",
            "mail": "cyliu@163.com"
        }))
