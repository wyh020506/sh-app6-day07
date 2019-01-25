from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver


    def search_element(self, loc, timeout=15, poll_frequency=1):
        """
        定位单个元素
        :param loc: 元祖 (By.ID,id属性值) (By.CLASS_NAME,class属性值) (By.XPATH,xpath属性值)
        :param timeout: 搜索元素超时时间
        :param poll_frequency: 搜索间隔
        :return: 元素定位对象
        """

        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))
    def search_elements(self, loc, timeout=15, poll_frequency=1):
        """
        定位单个元素
        :param loc: 元祖 (By.ID,id属性值) (By.CLASS_NAME,class属性值) (By.XPATH,xpath属性值)
        :param timeout: 搜索元素超时时间
        :param poll_frequency: 搜索间隔
        :return: 元素定位对象
        """

        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=15, poll_frequency=1):
        """
        点击元素操作
        :param loc: 元祖 (By.ID,id属性值) (By.CLASS_NAME,class属性值) (By.XPATH,xpath属性值)
        :param timeout: 搜索元素超时时间
        :param poll_frequency: 搜索间隔
        :return:
        """
        self.search_element(loc, timeout, poll_frequency).click()

    def send_element(self, loc, text,timeout=15, poll_frequency=1):
        """
        输入内容操作
        :param loc: 元祖 (By.ID,id属性值) (By.CLASS_NAME,class属性值) (By.XPATH,xpath属性值)
        :param text: 输入内容
        :param timeout: 搜索元素超时时间
        :param poll_frequency: 搜索间隔
        :return:
        """
        # 定位元素
        input_text = self.search_element(loc, timeout, poll_frequency)
        # 清空
        input_text.clear()
        # 输入
        input_text.send_keys(text)