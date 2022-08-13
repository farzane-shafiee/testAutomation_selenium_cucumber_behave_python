import configparser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

config = configparser.RawConfigParser()
config.read("Configuration/config.ini")


class ReadConfig:

    @staticmethod
    def getCreateDriver():
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        return driver

    @staticmethod
    def getURL():
        url = config.get('common-info', 'baseURL')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common-info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common-info', 'password')
        return password
