import requests

from contact.my_token import WeiChat


class User:

    def creat(self, dict, token):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN",
                      params=token,
                      json=dict
                      ).json()

    def list(self, token, department_id=1):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                     params={"access_token": token, "department_id": department_id},
                     ).json()