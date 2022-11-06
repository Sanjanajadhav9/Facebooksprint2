import datetime

import pytest

from Library.excle_lib import ReadExcle
from POM.friends_module import FriendsPage
from Library.config import Configuration


class TestFriendsPage:
    obj = ReadExcle()
    data = obj.read_test_data(Configuration.FRIENDS_TEST_DATASHEET)

    @pytest.mark.parametrize("email, pwd", data)
    def test_click_login_link(self, init_driver, email, pwd):
        driver = init_driver
        try:
            lp = FriendsPage(driver)
            lp.user_name(email)
            lp.password_1(pwd)
            lp.login_1()
            lp.TC_Home_001()
            lp.TC_HOME_002()
            lp.TC_HOME_003()
            lp.TC_HOME_004()
            lp.TC_HOME_006()
            lp.TC_HOME_007()
            lp.TC_HOME_008()
            lp.TC_HOME_009()
            lp.TC_HOME_010()
            lp.TC_HOME_011()
            lp.TC_HOME_012()
            lp.TC_HOME_013()
            lp.TC_HOME_014()
            lp.TC_HOME_015()
            lp.TC_HOME_016()
            lp.TC_HOME_017()

        except BaseException as err_msg:
            td = datetime.datetime.now()
            name = f"screenshot1_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Configuration.SCREENSHOTS_PATH+name)
            raise err_msg



