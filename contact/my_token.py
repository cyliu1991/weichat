import requests
import yaml
import logging
import requests

class WeiChat:
    logging.basicConfig(level=logging.DEBUG)
    _token = ""
    @classmethod
    def get_token(cls):
        print("token"+cls._token)
        if len(cls._token) == 0:  # 预先判断token是否为空, 不为空时不再重新获取，减少函数调用次数
            conf = yaml.safe_load(open("WeiChat.yaml"))
            logging.debug(conf["env"])

            r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={"corpid": conf["env"]["corpid"],
                                 "corpsecret": conf["env"]["corpsecret"]}
                         ).json()
            cls._token = r["access_token"]
        else:
            return cls._token