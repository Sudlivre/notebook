from selenium import webdriver
import pytest
import contextlib


# PhantomJS - 无头浏览器
# ChromeDriver / FirefoxDriver
@pytest.fixture(scope='session')
def chrome():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_baidu_index(chrome):
    chrome.get('https://www.baidu.com')
    assert chrome.title == '百度一下，你就知道'

