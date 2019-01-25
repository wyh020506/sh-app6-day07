from Page.setting_page import SettingPage
from Page.more_page import MorePage
from Page.moile_network_page import MobileNetworkPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    def get_setting_page_obj(self):
        # 返回设置页面对象
        return SettingPage(self.driver)

    def get_more_page_obj(self):
        # 返回更多页面对象
        return MorePage(self.driver)

    def get_mobile_network_page_obj(self):
        # 返回移动网络设置页面对象
        return MobileNetworkPage(self.driver)
