# pip3 install selenium
# pip3 install webdriver-manager
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# browser = webdriver.Firefox()
# browser = webdriver.Firefox(r'./SynologyDrive/Repository/Python/seleniumSimpleTestWebDriver')
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get('https://www.youtube.com/')
print(browser.title)
browser.quit()
