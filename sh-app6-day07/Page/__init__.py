from selenium.webdriver.common.by import By


"""短信页面元素"""
# 添加短信按钮
add_sms_id = (By.ID, "com.android.mms:id/action_compose_new")
# 手机号
phone_id = (By.ID, "com.android.mms:id/recipients_editor")
# 输入短信内容
sms_text_id = (By.ID, "com.android.mms:id/embedded_text_editor")
# 发送按钮
sms_send_btn_id = (By.ID, "com.android.mms:id/send_button_sms")
# 获取结果
sms_result_ids = (By.ID, "com.android.mms:id/text_view")


"""设置页面"""
# 更多按钮
more_btn_xpath = (By.XPATH, "//*[contains(@text,'更多')]")
"""设置页面 -更多页面"""
# 移动网络
mobile_network_xpath = (By.XPATH, "//*[contains(@text,'移动')]")
"""设置页面 -更多页面 -移动网络页面"""
# 首选网络类型
one_network_xpath = (By.XPATH, "//*[contains(@text,'首选')]")
# 3G
set_network_3G_xpath = (By.XPATH, "//*[contains(@text,'3G')]")
# 取结果列表
set_network_list_ids = (By.ID, "android:id/summary")