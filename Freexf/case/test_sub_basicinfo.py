# coding:utf-8

import unittest
from selenium import webdriver
from page.loginpage import LoginPage
from page.basicInfopage import BasicInfo
from time import sleep

class TestSubBasicinfo(unittest.TestCase):
    name = "恬静一"
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.login = LoginPage(cls.driver)
        cls.basicinfo = BasicInfo(cls.driver)
        cls.login.login()


    def test01_subbasicinfo(self):

        self.basicinfo.sub_basic_info(nickname=self.name,y=2,m=3,d=1)
        sleep(3)
        res = self.basicinfo.get_username_title()
        self.assertTrue(res == self.name)

    def test02_subbasicinfo_name_null(self):
        '''------  昵称为空 ----- '''
        # self.login.login()
        # self.basicinfo.sub_basic_info(nickname="",y=2,m=3)
        # sleep(3)


        self.basicinfo.input_nickname(nickname="")
        print("----xingbie------")
        sleep(3)
        # self.click_sex()
        print("----shengrinian------")
        sleep(3)
        self.basicinfo.select_birthyear(y = 3)  # 这个？是的


        sleep(3)
        self.basicinfo.select_birthmonth(m = 4)
        sleep(3)
        print("bbbbbbbbbbbbbbbbb")
        # self.select_birthday(d)
        # sleep(3)
        # self.select_prvince(province)
        # sleep(3)
        # self.select_city(city)
        # sleep(3)
        # self.select_district(district)
        # sleep(3)
        # self.select_edu(education)
        sleep(3)
        self.basicinfo.click_sub_button()
        res = self.basicinfo.get_username_title()
        print(res)
        self.assertTrue(res == "您还没有昵称哟？")

    # def tearDown(self):
    #     self.login.logout()
    #     self.driver.quit()

    @classmethod
    def tearDownClass(cls):

        cls.login.logout()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()