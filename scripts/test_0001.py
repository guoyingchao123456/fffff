import allure

class Test_0001:
    @allure.step(title="测试步骤名称")
    def test_001(self):
        print("这是一个测试用例")
        assert True