# import time
#
# from behave import *
# from selenium import webdriver
#
#
# @when(u'Enter the Username"{username_}"')
# def enter_user_name(context, username_):
#     time.sleep(3)
#     context.driver.find_element("xpath", '//input[@id="email"]').send_keys(username_)
#     time.sleep(2)
#
#
# @when(u'Enter the Password"{pwd}"')
# def enter_password_btn(context, pwd):
#     context.driver.find_element("xpath", '//input[@id="pass"]').send_keys(pwd)
#     time.sleep(3)
#
#
# @when(u'Click on login button open')
# def login_btn(context):
#     context.driver.find_element("xpath", '//button[@name="login"]').click()
#     time.sleep(3)
#
#
# @when(u'Click on friends button open')
# def frd_btn_11(context):
#     context.driver.find_element("xpath", '//a[@aria-label="Friends"]').click()
#     time.sleep(3)
#
# @when(u'Click on all friend button')
# def all_frd_bt(context):
#     context.driver.find_element("xpath", '//span[text()="All Friends"]').click()
#     time.sleep(3)
# #
#
# @when(u'Click on search bar')
# def search_bar(context):
#     context.driver.find_element("xpath", '''//input[@class="x1i10hfl xggy1nq x1s07b3s x1kdt53j x1yc453h xhb22t3 xb5gni xcj1dhv x2s2ed0 xq33zhf xjyslct xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou xnwf7zb x40j3uw x1s7lred x15gyhx8 x9f619 xzsf02u xdl72j9 x1iyjqo2 xs83m0k xjb2p0i x6prxxf xeuugli x1a2a7pz x1n2onr6 x15h3p50 xm7lytj xsyo7zv xdvlbce x16hj40l xc9qbxq"]''').click()
#     time.sleep(3)
#
#
# @when(u'Click on search dot')
# def search_dot(context):
#     context.driver.find_element("xpath", '(//div[@aria-label="More"])[3]').click()
#     time.sleep(3)
#
#
# @when(u'Click on message button')
# def msg_btn(context):
#     context.driver.find_element("xpath", '(//div[@role="menuitem"])[1]').click()
#     time.sleep(3)
#     context.driver.find_element("css selector",'g[stroke-linecap="round"]').click()
#     time.sleep(2)
#     context.driver.find_element("xpath", '(//div[@aria-label="More"])[3]').click()
#     time.sleep(3)
#
# @when(u'Click on block button')
# def block_btn(context):
#     context.driver.find_element("xpath", '(//div[@role="menuitem"])[3]').click()
#     time.sleep(3)
#     context.driver.find_element("xpath",'//div[@aria-label="Cancel"]').click()
#
#
# @then(u'Click on unfriend button')
# def unfrd_btn(context):
#     context.driver.find_element("xpath", '(//div[@aria-label="More"])[3]').click()
#     time.sleep(3)
#     context.driver.find_element("xpath", '(//div[@role="menuitem"])[4]').click()
#     time.sleep(3)
#     context.driver.find_element("xpath",'//span[text()="Cancel"]').click()
#     time.sleep(3)
#     context.driver.close()
#
# @when(u'Click on friends button open_1')
# def frd_btn_11(context):
#     context.driver.find_element("xpath", '//a[@aria-label="Friends"]').click()
#     time.sleep(3)
#
#
# @then(u'Click on friends button open_2')
# def frd_btn_11(context):
#     context.driver.find_element("xpath", '//a[@aria-label="Friends"]').click()
#     time.sleep(3)
#
# @then(u'Click on custom list')
# def custom_list(context):
#     context.driver.find_element("xpath", '//span[text()="Custom lists"]').click()
#     time.sleep(3)
#
# @then(u'Click on close friend button')
# def close_frd_btn(context):
#     context.driver.find_element("xpath", '//span[text()="Close friends"]').click()
#     time.sleep(3)
#
# @then(u'Click on fav button')
# def fav_btn(context):
#     context.driver.find_element("xpath", '//span[text()="fav"]').click()
#     time.sleep(3)
#
# @then(u'Click on frds button')
# def frds_btn(context):
#     context.driver.find_element("xpath", '//span[text()="frds"]').click()
#     time.sleep(3)
#
# @then(u'Click on friends button open_3')
# def frd_btn_11(context):
#     context.driver.find_element("xpath", '//a[@aria-label="Friends"]').click()
#     time.sleep(3)
#
# @then(u'Click on notification settings button')
# def noti_setting_btn(context):
#     context.driver.find_element("xpath", '//div[@class="x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 x14yjl9h xudhj91 x18nykt9 xww2gxu x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 xl56j7k xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xc9qbxq x14qfxbe x1qhmfi1"]').click()
#     time.sleep(3)
#
# @then(u'Click on notification dot button')
# def noti_dot(context):
#     context.driver.find_element("xpath", '//input[@class="x1i10hfl x9f619 xggy1nq x1s07b3s x1ypdohk x5yr21d xdj266r x11i5rnm xat24cr x1mh8g0r x1w3u9th x1a2a7pz xexx8yu x4uap5 x18d9i69 xkhd6sd x10l6tqk x17qophe x13vifvy xh8yej3"]').click()
#     time.sleep(3)
#     context.driver.close()
#
#
#
