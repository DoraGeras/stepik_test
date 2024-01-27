import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.fixture(scope='function')
def answer():

    return str(math.log(int(time.time())))


class TestStepik:
    @classmethod
    def setup_class(cls):

        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(5)

    @classmethod
    def teardown_class(cls):

        cls.browser.quit()

    @pytest.mark.parametrize('link', links)
    def test_stepik(self, link, answer):

        self.browser.get(link)

        textarea = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
        )

        textarea.send_keys(answer)

        self.browser.find_element(By.CSS_SELECTOR,'button.submit-submission ').click()

        feedback = self.browser.find_element(By.CSS_SELECTOR,'pre.smart-hints__hint').text

        assert feedback == 'Correct!'