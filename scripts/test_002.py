import allure


class Test_002:

    def test_add_png(self):
        with open("C:\\Users\\xuly\\Desktos\\App08\\scripts\\abc.png", "rb") as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)
