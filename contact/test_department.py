from contact.my_token import WeiChat


class TestDepartment:
    @classmethod
    def setup_class(cls):
        WeiChat.get_token()
        print(WeiChat.token)

    def setup(self):
        print("setup")

    def test_creat(self):
        pass