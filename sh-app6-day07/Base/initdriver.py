from appium import webdriver


def get_driver(pac, act):
    """
    声明driver 对象
    :param pac: 包名
    :param act: 启动名
    :return: driver对象
    """
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app的信息
    desired_caps['appPackage'] = pac
    desired_caps['appActivity'] = act
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明我们的driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)