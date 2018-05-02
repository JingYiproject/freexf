# coding:utf-8
from common.base import BasePage
from time import sleep

class BasicInfo(BasePage):
    user_ico_loc = ("css selector",".i-icon.user-icon")
    basic_loc = ("xpath",".//*[@id='form1']/div[3]/div[1]/div[2]/div[4]/div/ul/a[1]/li")
    name_loc = ("class name","user-imfor-input")
    sex_loc = ("css selector","radio>i")
    year_loc = ("id","selectpick_icon_select_year")  # 页面呢，这个是低级问题啊，class属性有空格时候，第二课就讲了.zhiya
    yead_selc_loc = ("css selector", ".selectpick_ul_select_year>li")
    month_loc = ("id","selectpick_icon_select_month")
    month_selc_loc=("css selector",".selectpick_ul_select_month>li")
    day_loc = ("id","selectpick_icon_select_day")
    day_selc_loc=("css selector",".selectpick_ul_select_day>li")

    address_prvince_loc = ("css selector","#address-province>span")
    address_city_loc = ("css selector","#address-city>span")
    address_district_loc = ("css selector","#address-district>span")
    education_loc = ("css selector","#selectpick_select_education")
    sub_loc = ("id","ctl00_ContentPlaceHolder1_UCmd_submit")
    username_loc = ("css selector",".username-title")

    def move_usericon(self):
        self.move_to_element(self.user_ico_loc)
    def click_basic_button(self):

        self.click(self.basic_loc)

    def input_nickname(self,nickname):

        self.send_keys(self.name_loc,nickname)

    def click_sex(self):
        self.click(self.sex_loc)

    def select_birthyear(self,y):

        self.click(self.year_loc)  # 先点开选项卡
        sleep(1)
        elems = self.find_elements(self.yead_selc_loc) # 再点选项
        elems[y].click()       #点第几个
        # self.select_by_text(self.year_loc,ye ar) # 这个根本不是selct，又在瞎写，第三节课内容

    def select_birthmonth(self,m):
        self.click(self.month_loc)  # 先点开选项卡
        sleep(1)
        elems = self.find_elements(self.month_selc_loc) # 再点选项
        elems[m].click()       #点第几个

    def select_birthday(self,d):
        self.click(self.day_loc)  # 先点开选项卡
        sleep(1)
        elems = self.find_elements(self.day_selc_loc) # 再点选项
        elems[d].click()       #点第几个

    def select_prvince(self,province):
        self.select_by_text(self.address_prvince_loc,province)

    def select_city(self,city):
        self.select_by_text(self.address_city_loc,city)

    def select_district(self,district):
        self.select_by_text(self.address_district_loc,district)

    def select_edu(self,education):
        self.select_by_text(self.education_loc,education)

    def click_sub_button(self):
        self.click(self.sub_loc)

    def sub_basic_info(self,nickname="tianjingyi",y=1,m=2,d =3,province="河南省",city="洛阳市",district="洛龙区",
                       education="本科"):
        print("-------移动---------")
        sleep(3)
        self.move_usericon()
        print("----------点击-------")
        sleep(3)
        self.click_basic_button()
        print("----shurumingzi------")
        sleep(3)
        self.input_nickname(nickname)
        print("----xingbie------")
        sleep(3)
        # self.click_sex()
        print("----shengrinian------")
        sleep(3)
        self.select_birthyear(y)  # 这个？是的


        sleep(3)
        self.select_birthmonth(m)
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
        self.click_sub_button()

    def get_username_title(self):
        try:
            res = self.find_element(self.username_loc).text

            return res

        except:
            print("提交失败！！！返回空字符串")
            return ""

if __name__=="__main__":
    from  selenium import webdriver
    from page.loginpage import LoginPage
    driver = webdriver.Firefox()
    login = LoginPage(driver)
    login.login()
    print("---------11111111111111---------")
    basicinfo = BasicInfo(driver)
    print("-------------2222222222222222222-------")
    basicinfo.sub_basic_info()
    print(basicinfo.get_username_title())








