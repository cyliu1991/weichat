import requests
import yaml
import logging
import requests

class WeiChat:
    logging.basicConfig(level=logging.DEBUG)
    token = ""
    @classmethod
    def get_token(cls):
        print("token"+cls.token)
        if len(cls.token) == 0:
            conf = yaml.safe_load(open("WeiChat.yaml"))
            logging.debug(conf["env"])

            r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={"corpid": conf["env"]["corpid"],
                                 "corpsecret": conf["env"]["corpsecret"]}
                         ).json()
            cls.token = r["access_token"]
        else:
            return cls.token