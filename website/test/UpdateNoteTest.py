from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import override_settings
from selenium.webdriver.common.keys import Keys
from website.test.LoginMethod import login
from website.test.LoginMethod import login2
from website.test.LoginMethod import login3
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep



#Requirement 4
@override_settings(DEBUG=True)
class UpdateFolderTestCase(StaticLiveServerTestCase):
    fixtures = ['user-data-note-update.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        cls.selenium = WebDriver(executable_path="D:/School/geckodriver.exe")
        cls.selenium.implicitly_wait(10)



    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    #Test edit shared note
    def test_update_shared_note(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/note/e6880768-a7e8-4285-983b-6d133e8d5e31/sharedupdate/'))
        login3(self)

        tiny_frame = self.selenium.find_element_by_id('id_text_ifr')
        self.selenium.switch_to.frame(tiny_frame)
        editor_body = self.selenium.find_element_by_id("tinymce")
        editor_body.clear()
        editor_body.send_keys('Edited this now!')
        self.selenium.switch_to.default_content()

        update_button = self.selenium.find_element_by_xpath('//button[@type="submit"]')
        self.selenium.execute_script("arguments[0].scrollIntoView();", update_button)
        update_button.location_once_scrolled_into_view
        sleep(1)
        update_button.click()

        self.selenium.find_element_by_id('shared-notes').click()
        self.selenium.find_element_by_xpath('//div[@id="shared-notes-view"]/form/div/a/i').click()

        tinyframe = self.selenium.find_element_by_id('id_text_ifr')
        self.selenium.switch_to.frame(tinyframe)
        text_body = self.selenium.find_element_by_id("tinymce").text
        self.selenium.switch_to.default_content()

        self.assertEquals('Edited this now!', text_body, 'Shared note successfully updated!')


    #Test edit text in local note
    def test_update_local_note(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/note/d2fa6d19-d966-4b1e-8961-14653ec84fb6/update/'))
        login3(self)

        tiny_frame = self.selenium.find_element_by_id('id_text_ifr')
        self.selenium.switch_to.frame(tiny_frame)
        editor_body = self.selenium.find_element_by_id("tinymce")
        editor_body.clear()
        editor_body.send_keys('Edited this now!')
        self.selenium.switch_to.default_content()

        update_button = self.selenium.find_element_by_xpath('//button[@type="submit"]')
        self.selenium.execute_script("arguments[0].scrollIntoView();", update_button)
        update_button.location_once_scrolled_into_view
        sleep(1)
        update_button.click()

        self.selenium.find_element_by_xpath('//button[@id="fc1fb5d4-a214-4590-9ab7-22edcc888a1d"]/h4').click()
        sleep(1)
        self.selenium.find_element_by_xpath('//div[@id="notes"]/form/div/a').click()
        sleep(1)

        tinyframe = self.selenium.find_element_by_id('id_text_ifr')
        self.selenium.switch_to.frame(tinyframe)
        text_body = self.selenium.find_element_by_id("tinymce").text
        self.selenium.switch_to.default_content()

        self.assertEquals('Edited this now!', text_body, 'Local note successfully updated!')


    #Test edit file name in local note
    def test_update_note_name(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/note/d2fa6d19-d966-4b1e-8961-14653ec84fb6/update/'))
        login3(self)

        self.selenium.find_element_by_name('file_name').send_keys('edit_changed')

        update_button = self.selenium.find_element_by_xpath('//button[@type="submit"]')
        update_button.location_once_scrolled_into_view
        sleep(1)
        update_button.click()

        self.selenium.find_element_by_xpath('//button[@id="fc1fb5d4-a214-4590-9ab7-22edcc888a1d"]/h4').click()

        found = self.selenium.find_elements_by_xpath('//h4[contains(.,"edit_changed")]')

        self.assertTrue(found, 'The edit_changed element should be present')

    #Test edit folder location of local note
    def test_update_note_folder(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/note/d2fa6d19-d966-4b1e-8961-14653ec84fb6/update/'))
        login3(self)

        select = Select(self.selenium.find_element_by_id('id_folder'))
        select.select_by_visible_text('second_folder')

        update_button = self.selenium.find_element_by_xpath('//button[@type="submit"]')
        update_button.location_once_scrolled_into_view
        sleep(1)
        update_button.click()
    
        self.selenium.find_element_by_xpath('//button[@id="f93ee100-ba9a-4e86-b02f-1ca7fde87979"]/h4').click()

        found = self.selenium.find_elements_by_xpath('//h4[contains(.,"test_edit")]')

        self.assertTrue(found, 'The test_edit element should be present')
