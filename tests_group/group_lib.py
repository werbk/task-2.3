from fixture.TestBase import BaseClass
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.variables import UserLogin


class Group:
    def __init__(self, group_name, group_header, group_footer):
        self.group_name = group_name
        self.group_header = group_header
        self.group_footer = group_footer


class GroupBase():
    def __init__(self):
        # This code duplicated in GroupBase & ContractBase, if do like says in video. How i can fix it?
        # self.wd = WebDriver()
        # self.wd.implicitly_wait(60)


        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        #self.session.login(UserLogin.name, UserLogin.password)
        self.session = BaseClass(self)

    def create_group(self, Group):
        wd = self.wd
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.group_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Group.group_footer)
        wd.find_element_by_name("submit").click()

    def delete_first_group(self):
        wd = self.wd
        self.wd.find_element_by_link_text("groups").click()
        self.wd.find_element_by_css_selector("span.group").click()
        if not self.wd.find_element_by_name("selected[]").is_selected():
            self.wd.find_element_by_name("selected[]").click()
        self.wd.find_element_by_xpath("//div[@id='content']/form/input[5]").click()

    def click_group_page(self):
        wd = self.wd
        wd.find_element_by_css_selector("div.msgbox").click()
        wd.find_element_by_link_text("group page").click()

    def restore_group(self):
        self.wd.quit()