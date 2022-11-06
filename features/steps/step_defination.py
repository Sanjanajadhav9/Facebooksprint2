# import time
#
# from behave import *
# from selenium import webdriver
#
#
# @given(u'Open the browser and enter the valid url')
# def launch_browser(context):
#     context.driver = webdriver.Chrome()
#     context.driver.get("https://www.facebook.com/")
#     context.driver.maximize_window()
#     time.sleep(8)
#
#
# @then(u'Click on login button')
# def login_btn(context):
#     context.driver.find_element("xpath", '//button[@name="login"]').click()
#     time.sleep(3)
#     context.driver.close()
#
#
# @when(u'Click on login button')
# def click_login_btn(context):
#     context.driver.find_element("xpath", '//button[@name="login"]').click()
#     time.sleep(3)
#
#
# @when(u'Click on friends button')
# def frd_btn(context):
#     time.sleep(6)
#     context.driver.find_element("xpath", '//a[@aria-label="Friends"]').click()
#     time.sleep(3)
#
#
# @then(u'Click on friend request button')
# def frd_req_btn(context):
#     context.driver.find_element("xpath", '(//div[@aria-label="Friends"])[1]//span[text()="Friend requests"]').click()
#     context.driver.close()
#
#
# @then(u'Click on suggestion button')
# def suggestion_btn(context):
#     context.driver.find_element("xpath", '//span[text()="Suggestions"]').click()
#     time.sleep(3)
#     context.driver.close()
#
#
