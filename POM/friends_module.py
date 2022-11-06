import re
import time

from Library.excle_lib import ReadExcle
from Library.config import Configuration


class FriendsPage:
    obj_1 = ReadExcle()
    locator_reg = obj_1.read_locator(Configuration.FRIENDS_LOCATOR_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def user_name(self, username):
        locator = self.locator_reg["username"]
        result = re.findall(r"\w+@gmail\.com", username)
        assert result != [] , "invalid username"
        self.driver.find_element(*locator).send_keys(username)

    def password_1(self, pwd):
        locator = self.locator_reg["password_txt"]
        self.driver.find_element(*locator).send_keys(pwd)
        time.sleep(3)

    def login_1(self):
        locator = self.locator_reg["login_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def TC_Home_001(self):
        locator = self.locator_reg["friends_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(3)


    def TC_HOME_002(self):
        locator = self.locator_reg["frd_req"]
        self.driver.find_element(*locator).click()
        time.sleep(4)
        locator = self.locator_reg["friends_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(3)


    def TC_HOME_003(self):
        locator = self.locator_reg["suggestion"]
        self.driver.find_element(*locator).click()
        time.sleep(3)
        locator = self.locator_reg["friends_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(3)


    def TC_HOME_004(self):
        locator = self.locator_reg["all_frd"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def TC_HOME_005(self):
        locator = self.locator_reg["search"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def TC_HOME_006(self):
        locator = self.locator_reg["search_dot"]
        self.driver.find_element(*locator).click()
        time.sleep(4)

    def TC_HOME_007(self):
        locator = self.locator_reg["msg"]
        self.driver.find_element(*locator).click()
        time.sleep(4)
        locator = self.locator_reg["back_1"]
        self.driver.find_element(*locator).click()
        time.sleep(4)
        locator = self.locator_reg["more_1"]
        self.driver.find_element(*locator).click()
        time.sleep(4)


    def TC_HOME_008(self):
        locator = self.locator_reg["block"]
        self.driver.find_element(*locator).click()
        time.sleep(3)
        locator = self.locator_reg["cancel_block"]
        self.driver.find_element(*locator).click()
        time.sleep(3)


    def TC_HOME_009(self):
        locator = self.locator_reg["unfriend"]
        self.driver.find_element(*locator).click()
        time.sleep(3)
        locator = self.locator_reg["unfrd_back"]
        self.driver.find_element(*locator).click()
        time.sleep(3)
        locator = self.locator_reg["unfrd_cancel"]
        self.driver.find_element(*locator).click()
        time.sleep(3)
        locator = self.locator_reg["friends_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(3)


    def TC_HOME_010(self):
        locator = self.locator_reg["birthday"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def TC_HOME_011(self):
        locator = self.locator_reg["name_click"]
        self.driver.find_element(*locator).click()
        time.sleep(3)
        locator = self.locator_reg["friends_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def TC_HOME_012(self):
        locator = self.locator_reg["custom_list"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def TC_HOME_013(self):
        locator = self.locator_reg["close_frd"]
        self.driver.find_element(*locator).click()
        time.sleep(3)


    def TC_HOME_014(self):
        locator = self.locator_reg["fav"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def TC_HOME_015(self):
        locator = self.locator_reg["frds"]
        self.driver.find_element(*locator).click()
        time.sleep(3)
        locator = self.locator_reg["friends_btn"]
        self.driver.find_element(*locator).click()
        time.sleep(3)


    def TC_HOME_016(self):
        locator = self.locator_reg["notification_setting"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def TC_HOME_017(self):
        locator = self.locator_reg["notification_dot"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

