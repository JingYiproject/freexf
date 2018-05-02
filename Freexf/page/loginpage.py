# coding:utf-8

from common.base import BasePage

class LoginPage(BasePage):
    '''登录页面'''
    alert_loc = ("class name","ui-dialog-autofocus")
    login_but_loc = ("xpath","//*[@id='index_login']/span")
    user_loc = ("id","Header_Login_UTxt_UserName")
    psw_loc = ("id","Header_Login_UTxt_Password")
    sub_loc = ("class name","dialog-login-button")
    shoucang_loc = ("css selector",".user-photo-icon.s-1")

    def open_login_page(self):
        self.driver.get("http://freexf.com/")

    def click_alert_button(self):
        self.click(self.alert_loc)

    def click_login_button(self):
        self.click(self.login_but_loc)

    def input_username(self,username):
        self.send_keys(self.user_loc,username)

    def input_psw(self,psw):
        self.send_keys(self.psw_loc,psw)

    def click_sub_button(self):

        self.click(self.sub_loc)

    def login(self,username="15637168735",psw="tyjchj357"):

        self.open_login_page()
        self.click_alert_button()
        self.click_login_button()
        self.input_username(username)
        self.input_psw(psw)
        self.click_sub_button()

    def get_login_result(self):
        '''获取登录的结果'''
        try:
            self.find_element(self.shoucang_loc)
            print("登录成功！！！！")

        except:
            print("登录失败！！！！，返回空字符")
            return ""

    def logout(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Firefox()
    loginpage = LoginPage(driver)
    loginpage.login()
    loginpage.get_login_result()
    loginpage.logout()
    # driver.quit()




