from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

a=10
print(a)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org")
driver.fullscreen_window
driver.close