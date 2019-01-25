from Base.base import Base
import Page

class MorePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_mobile_btn(self):
        # 点击移动网络
        self.click_element(Page.mobile_network_xpath)