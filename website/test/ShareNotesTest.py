from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import override_settings
from selenium.webdriver.common.keys import Keys
from website.test.LoginMethod import login
from website.test.LoginMethod import login2
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep



#Requirement 11
@override_settings(DEBUG=True)
class ShareNotesTestCase(StaticLiveServerTestCase):
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
        
    #Test sharing a note not editable
    def test_share_note_edit(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/sharing/create'))
        login(self)

        persondrop = Select(self.selenium.find_element_by_id('id_person'))

        persondrop.select_by_visible_text("test_user_2")

        notedrop = Select(self.selenium.find_element_by_id('id_note'))

        notedrop.select_by_visible_text("test_note1_folder1")

        self.selenium.find_element_by_xpath('//*[@id="id_editor"]').click()

        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()


        self.selenium.find_element_by_xpath('/html/body/nav/form/a').click()

        self.selenium.get('%s%s' % (self.live_server_url, '/note/2da7df71-9b8a-40d0-86ca-5ade86dae31f/sharedupdate/'))

        login2(self)

        actualUrl = self.selenium.current_url.split("/", 3)[-1]

        self.assertEquals('note/2da7df71-9b8a-40d0-86ca-5ade86dae31f/sharedupdate/', str(actualUrl), 'Once shared this url should be accessible')
        
    #Test sharing a note not editable
    def test_share_note_view(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/sharing/create'))
        login(self)

        persondrop = Select(self.selenium.find_element_by_id('id_person'))

        persondrop.select_by_visible_text("test_user_2")

        notedrop = Select(self.selenium.find_element_by_id('id_note'))

        notedrop.select_by_visible_text("test_note1_folder1")

        self.selenium.find_element_by_xpath('/html/body/div/form/button').click()


        self.selenium.find_element_by_xpath('/html/body/nav/form/a').click()

        self.selenium.get('%s%s' % (self.live_server_url, '/note/2da7df71-9b8a-40d0-86ca-5ade86dae31f/view/'))

        login2(self)

        actualUrl = self.selenium.current_url.split("/", 3)[-1]

        self.assertEquals('note/2da7df71-9b8a-40d0-86ca-5ade86dae31f/view/', str(actualUrl), 'Once shared this url should be accessible')
        

        



