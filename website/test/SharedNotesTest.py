
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import override_settings
from selenium.webdriver.common.keys import Keys
from website.test.LoginMethod import login
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep



#Requirement 12
@override_settings(DEBUG=True)
class SharedNotesTestCase(StaticLiveServerTestCase):
    fixtures = ['user-data-folder.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        cls.selenium = WebDriver(executable_path="D:/School/geckodriver.exe")
        cls.selenium.implicitly_wait(10)



    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    # Test the edit feature on a shared note
    def test_edit_shared_note(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/note/45fe75a5-e173-4528-9166-3dcfcc2293da/sharedupdate/'))
        login(self)
        self.selenium.switch_to.frame(self.selenium.find_element_by_id("id_text_ifr"))

        text_input = self.selenium.find_element_by_id("tinymce")

        text_input.send_keys("this is a ")


        self.selenium.switch_to.default_content()

        update_button = self.selenium.find_element_by_xpath('/html/body/div[1]/form/button')

        self.selenium.execute_script("arguments[0].scrollIntoView();", update_button)
        
        update_button.location_once_scrolled_into_view
        sleep(1)

        update_button.click()

        self.selenium.get('%s%s' % (self.live_server_url, '/note/45fe75a5-e173-4528-9166-3dcfcc2293da/sharedupdate/'))

        self.selenium.switch_to.frame(self.selenium.find_element_by_id("id_text_ifr"))

        text = self.selenium.find_element_by_id("tinymce").get_attribute("innerHTML")

        

        self.assertEquals("<p>this is a test</p>", str(text), "Text should have been changed from `test` to `this is a test`")



    # Test the view feature on a shared note
    def test_view_shared_note(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/note/6d566040-3562-4cb1-92b5-909cddf2d130/view/'))
        login(self)
        self.selenium.implicitly_wait(10)

        text = self.selenium.find_element_by_xpath('/html/body/div/div/div/p').text

        self.assertEquals("test reee", text, "Text should read `test reee`")

        







    