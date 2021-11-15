from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup


class Barnesandnoble:
    def __init__(self):
        self.executable_path = r".\src\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.executable_path)
        self.error_message = ''
        self.Navigate_to_barnesandnoble()
        self.find_forget_password()
        self.get_error_message()

    def Navigate_to_barnesandnoble(self):
        self.driver.get('https://www.barnesandnoble.com/h/books/browse')
        # Wait for the webpage to load
        self.driver.implicitly_wait(3)

    def find_forget_password(self):
        # hover over my account element
        element_to_hover_over = self.driver.find_element_by_xpath('//*[@id="navbarDropdown"]')
        ActionChains(self.driver).move_to_element(element_to_hover_over).perform()

        # click create account
        self.driver.find_element_by_xpath('//a[@id="rhfCreateAcctLink"]').click()
        # wait for the popup to load
        self.driver.implicitly_wait(4)
        # change focus  on the iframe
        sign_up_frame = self.driver.find_element_by_xpath('//iframe[@title="Create an Account"]')
        self.driver.switch_to.frame(sign_up_frame)
        # wait for popup to load
        self.driver.implicitly_wait(1)
        # click on sign in link
        self.driver.find_element_by_xpath('//*[@id="loginModalLink"]').click()
        # wait for popup to load
        self.driver.implicitly_wait(3)
        # return to the parent frame
        self.driver.switch_to.parent_frame()
        # select sign up iframe
        sign_in_frame = self.driver.find_element_by_xpath('//iframe[@title="Sign in or Create an Account"]')
        self.driver.switch_to.frame(sign_in_frame)
        # click forget password
        self.driver.find_element_by_xpath('//*[@id="loginForgotPassword"]').click()
        # wait for popup to load
        self.driver.implicitly_wait(3)
        # select Password Assistance iframe

    def get_error_message(self):
        # select Password Assistance iframe
        self.driver.switch_to.parent_frame()
        f_password_frame = self.driver.find_element_by_xpath('//iframe[@title="Password Assistance"]')
        self.driver.switch_to.frame(f_password_frame)
        # make sure the input there is no data on it
        self.driver.find_element_by_xpath('//*[@id="email"]').clear()
        # set input value with my email
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('ramygharib91@gmail.com')
        # click submit
        self.driver.find_element_by_xpath('//*[@id="resetPwSubmit"]').click()

        self.driver.implicitly_wait(4)
        # check error
        self.error_message = self.driver.find_element_by_xpath('//*[@id="passwordAssistantErr"]/em').text

        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath('//*[@id="resetPwSubmit"]').click()

        # get error message using BeautifulSoup #

        # print(self.error_message)
        # html = self.driver.page_source
        # soup = BeautifulSoup(html, 'html.parser')
        # error_message = soup.find('aside', {'id': 'passwordAssistantErr'}).find('em')
        # self.error_message = error_message.get_text()
        return self.error_message


print(Barnesandnoble().error_message)
