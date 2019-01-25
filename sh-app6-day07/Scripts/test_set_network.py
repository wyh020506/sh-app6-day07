import sys, os
sys.path.append(os.getcwd())

from Page.setting_page import SettingPage
from Page.more_page import MorePage
from Page.moile_network_page import MobileNetworkPage

from Base.page import Page
from Base.initdriver import get_driver
import pytest


class Test_Set_Network:

    def setup_class(self):
        # 声明driver
        self.driver = get_driver("com.android.settings", ".Settings")
        # # 实例化设置页面类
        # self.setting_obj = SettingPage(self.driver)
        # # 实例化更多页面类
        # self.more_page = MorePage(self.driver)
        # # 实例化移动网络页面类
        # self.mobil_obj = MobileNetworkPage(self.driver)
        # 实例化统一入口类
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def in_mobile_setting(self):
        # 进入移动网络页面
        # 点击更多
        # self.setting_obj.click_more_btn()
        self.page_obj.get_setting_page_obj().click_more_btn()
        # 点击移动网络
        # self.more_page.click_mobile_btn()
        self.page_obj.get_more_page_obj().click_mobile_btn()

    def test_set_network(self):
        # 测试网络修改
        # 点击首选网络类型
        # self.mobil_obj.click_one_network()
        self.page_obj.get_mobile_network_page_obj().click_one_network()
        # 选择3G网络
        # self.mobil_obj.set_network_type(1)
        self.page_obj.get_mobile_network_page_obj().set_network_type(1)

        # 取结果列表 断言
        # assert "3G" in self.mobil_obj.get_set_network_result()
        assert "3G" in self.page_obj.get_mobile_network_page_obj().get_set_network_result()