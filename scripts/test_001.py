import allure, pytest


class TestUn:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是一个测试步骤1")
    def test_001_1(self):
        print("---test_001_1")
        allure.attach("标题", "具体内容")

        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是一个测试步骤2")
    def test_001_2(self):
        print("---test_001_2")

        assert True

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="这是一个测试步骤3")
    def test_001_3(self):
        print("---test_001_3")

        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="这是一个测试步骤4")
    def test_001_4(self):
        print("---test_001_4")

        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="这是一个测试步骤5")
    def test_001_5(self):
        print("---test_001_5")

        assert True
