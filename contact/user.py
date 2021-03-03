import requests

from contact.my_token import WeiChat


class User:

    def creat(self, dict):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN",
                      params=WeiChat.get_token(),
                      json=dict
                      ).json()

    def list(self, department_id=1):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                     params={"access_token": WeiChat.get_token(), "department_id": department_id},
                     ).json()