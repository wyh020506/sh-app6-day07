from Base.base import Base
import Page

class MobileNetworkPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_one_network(self):
        # 点击首选网路类型
        self.click_element(Page.one_network_xpath)

    def set_network_type(self, num):
        # 设置网络类型 1：3G 2：2G
        if str(num) == "1":
            self.click_element(Page.set_network_3G_xpath)

    def get_set_network_result(self):
        # 获取设置网络结果列表
        network_result = self.search_elements(Page.set_network_list_ids)
        return [i.text for i in network_result]