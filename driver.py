from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless=new')
options.add_argument("--window-size=1920,1000")
options.add_argument("--disable-browser-side-navigation")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
