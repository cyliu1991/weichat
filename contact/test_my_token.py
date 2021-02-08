from contact.my_token import WeiChat


class TestWeiChat:
    def test_get_token(self):
        print(WeiChat.get_token())
        assert WeiChat.get_token() != ""   # 调用两次，实际只发一次请求
