from Base.base import Base
import Page

class SettingPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_more_btn(self):
        # 点击更多按钮
        self.click_element(Page.more_btn_xpath)
