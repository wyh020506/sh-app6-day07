from Base.base import Base
import Page

class SmsPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_add_sms(self):
        # 点击新增短信按钮
        self.click_element(Page.add_sms_id)

    def send_phone(self, phone):
        # 输入手机号方法
        self.send_element(Page.phone_id, phone)

    def send_sms(self, send_data):
        # 发送短信方法
        # 输入内容
        self.send_element(Page.sms_text_id, send_data)
        # 点击发送按钮
        self.click_element(Page.sms_send_btn_id)

    def get_sms_reults(self):
        # 获取已发送短信内容方法
        sms_result = self.search_elements(Page.sms_result_ids)
        return [i.text for i in sms_result]