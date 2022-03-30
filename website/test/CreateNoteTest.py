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



#Requirement 3
@override_settings(DEBUG=True)
class CreateNoteTestCase(StaticLiveServerTestCase):
    fixtures = ['user-data-file.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        cls.selenium = WebDriver(executable_path="D:/School/geckodriver.exe")
        cls.selenium.implicitly_wait(10)



    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    #Test create note without providing a name
    def test_create_file_no_name(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/note/create/'))
        login3(self)

        select = Select(self.selenium.find_element_by_id('id_folder'))

        self.selenium.find_element_by_name('file_name').clear()
        select.select_by_visible_text('test_folder')
        
        tiny_frame = self.selenium.find_element_by_id('id_text_ifr')
        self.selenium.switch_to.frame(tiny_frame)
        editor_body = self.selenium.find_element_by_id("tinymce")
        editor_body.send_keys('this is a test')
        self.selenium.switch_to.default_content()

        create_button = self.selenium.find_element_by_xpath('//button[@type="submit"]')
        self.selenium.execute_script("arguments[0].scrollIntoView();", create_button)
        create_button.location_once_scrolled_into_view
        sleep(1)
        create_button.click()

        actualUrl = self.selenium.current_url.split("/", 3)[-1]

        self.assertEquals('note/create/', actualUrl, 'Note should not be able to be created without name')

    #Test create note without providing a folder
    def test_create_file_no_folder(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/note/create/'))
        login3(self)

        select = Select(self.selenium.find_element_by_id('id_folder'))
        self.selenium.find_element_by_xpath('//*[@id="id_file_name"]').send_keys('test_file')
        select.select_by_visible_text('---------')
        
        tiny_frame = self.selenium.find_element_by_id('id_text_ifr')
        self.selenium.switch_to.frame(tiny_frame)
        editor_body = self.selenium.find_element_by_id("tinymce")
        editor_body.send_keys('this is a test')
        self.selenium.switch_to.default_content()

        create_button = self.selenium.find_element_by_xpath('//button[@type="submit"]')
        self.selenium.execute_script("arguments[0].scrollIntoView();", create_button)
        create_button.location_once_scrolled_into_view
        sleep(1)
        create_button.click()

        actualUrl = self.selenium.current_url.split("/", 3)[-1]

        self.assertEquals('note/create/', actualUrl, 'Note should not be able to be created without choosing a folder')

    #Test create note without providing a body
    def test_create_file_no_body(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/note/create/'))
        login3(self)

        select = Select(self.selenium.find_element_by_id('id_folder'))
        self.selenium.find_element_by_name('file_name').send_keys('test_file')
        select.select_by_visible_text('test_folder')
        
        tiny_frame = self.selenium.find_element_by_id('id_text_ifr')
        self.selenium.switch_to.frame(tiny_frame)
        editor_body = self.selenium.find_element_by_id("tinymce")
        editor_body.clear()
        self.selenium.switch_to.default_content()

        create_button = self.selenium.find_element_by_xpath('//button[@type="submit"]')
        self.selenium.execute_script("arguments[0].scrollIntoView();", create_button)
        create_button.location_once_scrolled_into_view
        sleep(1)
        create_button.click()

        actualUrl = self.selenium.current_url.split("/", 3)[-1]

        self.assertEquals('note/create/', actualUrl, 'Note should not be able to be created without a body')

    #Test create note success
    def test_create_file_success(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/note/create/'))
        login3(self)

        self.selenium.find_element_by_name('file_name').send_keys('test_file')

        select = Select(self.selenium.find_element_by_id('id_folder'))
        select.select_by_visible_text('test_folder')
        
        tiny_frame = self.selenium.find_element_by_id('id_text_ifr')
        self.selenium.switch_to.frame(tiny_frame)
        editor_body = self.selenium.find_element_by_id("tinymce")
        editor_body.send_keys('this is a success test!')
        self.selenium.switch_to.default_content()

        create_button = self.selenium.find_element_by_xpath('//button[@type="submit"]')
        self.selenium.execute_script("arguments[0].scrollIntoView();", create_button)
        create_button.location_once_scrolled_into_view
        sleep(1)
        create_button.click()

        self.selenium.find_element_by_id('92fcef68-bc6f-439a-a034-0035e3fbc46e').click()

        found = self.selenium.find_elements_by_xpath('//h4[contains(.,"test_file")]')

        self.assertTrue(found, 'The test_file element should be present')

