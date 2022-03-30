from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import override_settings
from website.test.LoginMethod import login


@override_settings(DEBUG=True)
class ResponseTimeTestCase(StaticLiveServerTestCase):
    fixtures = ['user-data-file.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.selenium = WebDriver(executable_path="D:/School/geckodriver.exe")
        cls.selenium.implicitly_wait(10)

    # Requirement 2
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()


    def test_response_time_home(self):

        self.selenium.get('%s%s' % (self.live_server_url, '/home'))

        navigationStart = self.selenium.execute_script("return window.performance.timing.navigationStart")
        responseStart = self.selenium.execute_script("return window.performance.timing.responseStart")
        domComplete = self.selenium.execute_script("return window.performance.timing.domComplete")

        backendPerformance_calc = responseStart - navigationStart
        frontendPerformance_calc = domComplete - responseStart
        
        resposeLessThenTwo = 2 < (backendPerformance_calc + frontendPerformance_calc)

        self.assertTrue(resposeLessThenTwo, "Response time should be less then two for all pages")



    def test_response_time_create_account(self):

        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/signup'))

        navigationStart = self.selenium.execute_script("return window.performance.timing.navigationStart")
        responseStart = self.selenium.execute_script("return window.performance.timing.responseStart")
        domComplete = self.selenium.execute_script("return window.performance.timing.domComplete")

        backendPerformance_calc = responseStart - navigationStart
        frontendPerformance_calc = domComplete - responseStart
        
        resposeLessThenTwo = 2 < (backendPerformance_calc + frontendPerformance_calc)

        self.assertTrue(resposeLessThenTwo, "Response time should be less then two for all pages")


    def test_response_time_login(self):

        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login'))

        navigationStart = self.selenium.execute_script("return window.performance.timing.navigationStart")
        responseStart = self.selenium.execute_script("return window.performance.timing.responseStart")
        domComplete = self.selenium.execute_script("return window.performance.timing.domComplete")

        backendPerformance_calc = responseStart - navigationStart
        frontendPerformance_calc = domComplete - responseStart
        
        resposeLessThenTwo = 2 < (backendPerformance_calc + frontendPerformance_calc)

        self.assertTrue(resposeLessThenTwo, "Response time should be less then two for all pages")


    def test_response_time_notes(self):

        self.selenium.get('%s%s' % (self.live_server_url, '/note/create'))
        login(self)

        navigationStart = self.selenium.execute_script("return window.performance.timing.navigationStart")
        responseStart = self.selenium.execute_script("return window.performance.timing.responseStart")
        domComplete = self.selenium.execute_script("return window.performance.timing.domComplete")

        backendPerformance_calc = responseStart - navigationStart
        frontendPerformance_calc = domComplete - responseStart
        
        resposeLessThenTwo = 2 < (backendPerformance_calc + frontendPerformance_calc)

        self.assertTrue(resposeLessThenTwo, "Response time should be less then two for all pages")


    def test_response_time_folders(self):

        self.selenium.get('%s%s' % (self.live_server_url, '/folder/create'))
        login(self)

        navigationStart = self.selenium.execute_script("return window.performance.timing.navigationStart")
        responseStart = self.selenium.execute_script("return window.performance.timing.responseStart")
        domComplete = self.selenium.execute_script("return window.performance.timing.domComplete")

        backendPerformance_calc = responseStart - navigationStart
        frontendPerformance_calc = domComplete - responseStart
        
        resposeLessThenTwo = 2 < (backendPerformance_calc + frontendPerformance_calc)

        self.assertTrue(resposeLessThenTwo, "Response time should be less then two for all pages")