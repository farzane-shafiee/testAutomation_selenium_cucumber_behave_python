from datetime import datetime

import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium.webdriver.common.by import By
from Features.login.environment import *
from selenium.webdriver import ActionChains
from Utilities.readProperty import ReadConfig
from Utilities.customLogger import LogGen

baseURL = ReadConfig.getURL()
mylogger = LogGen.loggen()
login_link_xpath = '//a[text()=" ورود "]'
username_textbox_name = '//input[@name="username"]'
continue_button_xpath = ''
password_textbox_xpath = '//input[@name="password"]'
login_button_xpath = '//button[@class="btn btn-default"]'
assert_login = '(//a[text()!=""])[2]'
assert_not_login = '//h3[text()="اطلاعات وارد شده نامعتبر می باشد."]'


@given(u'open the site')
def step_open_site(context):
    context.driver = ReadConfig.getCreateDriver()
    mylogger.info('*** Driver initialized ***')
    context.driver.get(baseURL)
    mylogger.info('*** Get URL ***')
    WebDriverWait(context.driver, timeout=30)
    mylogger.info('*** Web Driver Wait ***')


@when(u'click on the login link')
def step_click_login_button(context):
    login = context.driver.find_element(By.XPATH, login_link_xpath)
    mylogger.info('*** Find the Login Link ***')
    login.click()
    mylogger.info('*** Click the Login Link ***')


@then(u'insert correct username "{username}"')
def step_insert_username(context, username):
    element_username = context.driver.find_element(By.XPATH, username_textbox_name)
    mylogger.info('*** Find the Username Input ***')
    element_username.click()
    mylogger.info('*** Click the Username Input ***')
    element_username.send_keys(username)
    mylogger.info('*** Send keys the Username Input ***')


@then(u'insert correct password "{password}"')
def step_insert_password(context, password):
    element_password = context.driver.find_element(By.XPATH, password_textbox_xpath)
    mylogger.info('*** Find the Password Input ***')
    element_password.click()
    mylogger.info('*** Click the Password Input ***')
    element_password.send_keys(password)
    mylogger.info('*** Send keys the Password Input ***')


@then(u'click the login button')
def step_click_login(context):
    action = ActionChains(context.driver)
    mylogger.info('*** Create ActionChains Driver ***')
    button = context.driver.find_element('xpath', login_button_xpath)
    mylogger.info('*** Find the Login Button ***')
    action.move_to_element(button).click().perform()
    mylogger.info('*** Click the Login Button ***')


@then(u'assertion login by "{username}"')
def step_assertion_login(context, username):
    actual_result_login = context.driver.find_element(By.XPATH, assert_login)
    mylogger.info('*** Find the Assert Login ***')
    if actual_result_login.text == f'{username} خوش آمدید':
        mylogger.info('*** If is True for Assert Login ***')
        context.driver.save_screenshot(
            './Screenshot/' + f'LoginPage_True_{str(datetime.now().strftime("%Y_%m_%d-%H_%M_%S"))}.png')
        allure.attach(context.driver.get_screenshot_as_png(), name="bookStore Login Test True",
                      attachment_type=AttachmentType.PNG)
        context.driver.close()
        mylogger.info('*** Close Driver ***')
    else:
        actual_result_not_login = context.driver.find_element(By.XPATH, assert_not_login)
        mylogger.info('*** Find the Assert Not Login ***')
        if actual_result_not_login.text == 'اطلاعات وارد شده نامعتبر می باشد.':
            mylogger.info('*** If is False for Assert Not Login ***')
            context.driver.save_screenshot(
                './Screenshot/' + f'LoginPage_False_{str(datetime.now().strftime("%Y_%m_%d-%H_%M_%S"))}.png')
            allure.attach(context.driver.get_screenshot_as_png(), name="bookStore Login Test False",
                          attachment_type=AttachmentType.PNG)
            context.driver.close()
            mylogger.info('*** Close Driver ***')
