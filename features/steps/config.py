from behave import *
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


from selenium import webdriver
from Constants.URLS import TestData
import logging
import os
from Pages.Login import login
from Pages.view_page import view_homepage


@given("Launch the browser")
def step_impl(context):
    if TestData.BROWSER == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=800,600")
        options.add_argument("--ignore-certificate-error")
        # options.add_argument("--ignore-ssl-errors")
        options.add_argument("--disable-notifications")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--allow-insecure-localhost")
        context.driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        context.driver.maximize_window()
    elif TestData.BROWSER == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--disable-notifications")
        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        logging.getLogger('WDM').setLevel(logging.NOTSET)
        os.environ['WDM_LOCAL'] = '1'
        os.environ['WDM_SSL_VERIFY'] = '0'

    elif TestData.BROWSER == 'edge':
        context.driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())


@then(u'Close the browser')
def step_impl(context):
    context.driver.close()
    context.driver.quit()
@when("Open the iris URL")
def step_impl(context):
    context.driver.get(TestData.iris_app_login_page)
    context.loginpage = login(context.driver)
    context.view = view_homepage(context.driver)
