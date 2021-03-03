import time

import pytest

from contact.my_token import WeiChat


@pytest.fixture(scope="session") # 在需要时自动创建并保存，适用于小型项目，封装较好时较少使用
def token():
    return WeiChat.get_token()

