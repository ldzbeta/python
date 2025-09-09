PROMISED_DOWN = 70
PROMISED_UP = 70
TWITTER_EMAIL = "known_un88842"
TWITTER_PASSWORD = "Killerman@10"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep,time
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

speed_website = "https://www.speedtest.net/"
twitter_website = "https://twitter.com/i/flow/login" 

options = Options()
options.binary_location = brave_path    
options.add_experimental_option("detach",True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options = options)
        self.up=0
        self.down=0

    def get_internet_speed(self):
        self.driver.get(speed_website)
        sleep(4)
        button=self.driver.find_element(By.CSS_SELECTOR,value=".start-button a")
        button.click()
        sleep(60)
        down_element=self.driver.find_element(By.CLASS_NAME,value="download-speed")
        upload_element=self.driver.find_element(By.CLASS_NAME,value="upload-speed")
        self.down = down_element.text
        self.up = upload_element.text

        print(self.down,self.up)
        

    
    def tweet_at_provider(self):
        self.driver.get(twitter_website)
        sleep(3)
        input_email=self.driver.find_element(By.NAME,value="text")
        input_email.send_keys(TWITTER_EMAIL)

        self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]').click()
        
        input_password=self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        input_password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)

        time.sleep(5)
        self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"

        text_box = self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div')
        text_box.send_keys(tweet)
        time.sleep(3)
        self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button').click()

        time.sleep(2)
        self.driver.quit()

twitter_bot=InternetSpeedTwitterBot()
# twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()