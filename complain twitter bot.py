import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

PROMISED_DOWN = 150
PROMISED_UP = 10
ACCOUNT_EMAIL = "KatiWatson4"
ACCOUNT_PASSWORD = "pythoncore100"


class InternetSpeedTwitterBot:
    def __init__(self, path):
        self.up = None
        self.down = None
        self.driver = webdriver.Chrome(path)

    def get_internet_speed(self):
        url = 'https://www.speedtest.net/'
        self.driver.get(url)
        click_go = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                     '1]/a/span[4]')
        click_go.click()
        time.sleep(60)
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                    '3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                      '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

        return self.down.text, self.up.text

    def tweet_at_provider(self, down_, up_):
        home_page = 'https://twitter.com/?lang=en-in'
        self.driver.get(home_page)
        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div['
                                                  '3]/a[2]/div')
        login.click()
        time.sleep(3)

        username = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username.send_keys(ACCOUNT_EMAIL)
        time.sleep(3)
        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(ACCOUNT_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div/span/br')
        tweet.send_keys(
            f'Hey Internet Provider,why is my internet speed {down_}down/{up_}up, when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?')
        time.sleep(3)
        button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        button.click()


path = ChromeDriverManager().install()
obj = InternetSpeedTwitterBot(path=path)
(down, up) = obj.get_internet_speed()
print(down, up)
obj.tweet_at_provider(down, up)
