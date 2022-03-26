def login(self):
    username_input = self.selenium.find_element_by_name("username")
    password_input = self.selenium.find_element_by_name("password")

    username_input.send_keys("test_user_correct")
    password_input.send_keys("testPassword_123")

    self.selenium.find_element_by_xpath('/html/body/div/form/button').click()