from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User

class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        self.user = User.objects.create_user(username="demo")
        self.user.set_password("12345")
        self.user.save()
        self.selenium.get(self.live_server_url)
        self.selenium.find_element(By.XPATH, '//button[text()="Play Now!"]').click()
        self.selenium.find_element(By.XPATH, "//input[@name='login']").click()
        self.selenium.find_element(By.XPATH, "//input[@name='login']").send_keys('demo')
        self.selenium.find_element(By.XPATH, "//input[@name='password']").click()
        self.selenium.find_element(By.XPATH, "//input[@name='password']").send_keys('12345')
        self.selenium.find_element(By.XPATH, '//button[text()="Login"]').click()
        self.selenium.find_element(By.XPATH, '//button[text()="profile"]').click()

    def test_profile(self):
        self.selenium.find_element(By.XPATH, '//button[text()="Items Inventory"]').click()
        self.selenium.find_element(By.XPATH, '//button[text()="Templates Inventory"]').click()
        self.selenium.find_element(By.XPATH, '//button[text()="Back"]').click()

    def test_upgrade(self):
        self.selenium.find_element(By.XPATH, '//button[text()="Upgrade"]').click()
        self.selenium.find_element(By.XPATH, "//button[@name='max_hp']").click()
        self.selenium.find_element(By.XPATH, "//button[@name='max_currency']").click()
        self.selenium.find_element(By.XPATH, "//button[@name='rate_currency']").click()
        self.selenium.find_element(By.XPATH, "//button[@name='awake']").click()
        self.selenium.find_element(By.XPATH, '//button[text()="Back"]').click()
        self.selenium.find_element(By.XPATH, '//button[text()="Back"]').click()
