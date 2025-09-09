from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep,time
# Path to your Brave executable
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# Target website
website = "https://www.deviceinfo.me/"
 
# Set up Chrome options and specify Brave as the binary
options = Options()
options.binary_location = brave_path    # Point to Brave brower
# options.add_argument('--headless')      # Optional: Run brower in headless mode
options.add_experimental_option("detach",True)
# Set up mobile emulation
mobile_emulation = {
    "deviceName": "Pixel 7"
}

options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# Create a Service object
# service = Service()

# Create a WebDriver instance
driver = webdriver.Chrome(options = options)

# Use the driver to open a website
driver.get(website)