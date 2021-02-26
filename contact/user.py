import requests

from contact.my_token import WeiChat


class User:

    def creat(self, dict):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN",
                      params=WeiChat.get_token(),
                      json=dict
                      ).json()
