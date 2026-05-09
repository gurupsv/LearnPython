# Import the 'modules' that are required for execution

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from time import sleep


# Fixture for Firefox
@pytest.fixture(scope="class")
def driver_init(request):
    options = FirefoxOptions()
    options.add_argument("--headless")
    try:
        ff_driver = webdriver.Firefox(options=options)
        request.cls.driver = ff_driver
        yield
        ff_driver.close()
    except Exception as e:
        pytest.skip(f"Firefox driver not available: {e}")


# Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    try:
        chrome_driver = webdriver.Chrome(options=options)
        request.cls.driver = chrome_driver
        yield
        chrome_driver.close()
    except Exception as e:
        pytest.skip(f"Chrome driver not available: {e}")


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class Test_URL(BasicTest):
    def test_open_url(self):
        self.driver.get("https://www.google.com/")
        print(self.driver.title)

        sleep(5)


@pytest.mark.usefixtures("chrome_driver_init")
class Basic_Chrome_Test:
    pass


class Test_URL_Chrome(Basic_Chrome_Test):
    def test_open_url(self):
        self.driver.get("https://www.google.com/")
        print(self.driver.title)

        sleep(5)
