import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Browser():
    def __init__(self):
        self.browser=webdriver.Edge()
        # self.browser.close()

    def StartBrowser(self,url):
        self.browser.get(url)
        self.browser.maximize_window()
        WebDriverWait(self.browser,10)
        return self.browser.page_source