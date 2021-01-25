from contact.my_token import WeiChat


class TestWeiChat:
    def test_get_token(self):
        assert WeiChat.get_token() != ""
