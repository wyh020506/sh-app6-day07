import os, sys
sys.path.append(os.getcwd())

from Page.sms_page import SmsPage
from Base.initdriver import get_driver
import pytest

class Test_Sms:

    def setup_class(self):
        # 声明driver
        self.driver = get_driver("com.android.mms", ".ui.ConversationList")
        # 实例化短信页面
        self.sms_obj = SmsPage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def addsms_sendphone(self):
        # 点击短信新建按钮 和 输入手机号码 13300001111
        self.sms_obj.click_add_sms()
        # 输入手机号
        self.sms_obj.send_phone("13300001111")

    @pytest.mark.parametrize("send_sms", ["123", "hello", "你好"])
    def test_send_sms(self, send_sms):
        # 测试发送短信方法 ["123", "hello", "你好"]
        self.sms_obj.send_sms(send_sms)
        # 获取结果列表
        assert send_sms in self.sms_obj.get_sms_reults()