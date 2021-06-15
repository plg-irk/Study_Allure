import allure
import time

from allure_commons.types import AttachmentType
from selenium import webdriver

exec_path = 'drivers/chromedriver.exe'

class TestPageSearch:

    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    # severity == blocker, critical, normal, minor, trivial,
    @allure.feature('Open page')
    @allure.story('Открываем страницу google.com')
    @allure.severity('blocker')
    def test_google_seach(self):
        self.driver.get('https://google.com')
        with allure.step('Делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot',
                          attachment_type=AttachmentType.PNG)
        assert self.driver.title == "Google"

    @allure.feature('Open page')
    @allure.story('Открываем страницу yandewx.ru')
    @allure.severity('critical')
    def test_yandex_seach(self):
        self.driver.get('https://yandex.ru')
        with allure.step('Делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot',
                          attachment_type=AttachmentType.PNG)
        assert self.driver.title == "Яндекс"

    @allure.feature('Open page')
    @allure.story('Открываем страницу mail.ru')
    @allure.severity('trivial')
    def test_mail_seach(self):
        self.driver.get('https://mail.ru')
        with allure.step('Делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot',
                          attachment_type=AttachmentType.PNG)
        assert 'Mail' in self.driver.title

# Для просмотра результатов тестов нужно в PowerShell набрать allure serve results
