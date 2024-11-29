"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser

from pages.home_page import signup_desktop, signup_mobile


@pytest.mark.parametrize('cross_browser', [(1920, 1080), (1366, 768)], indirect=True)
def test_github_desktop(cross_browser):
    browser.open('https://github.com/')
    signup_desktop()

    browser.quit()


@pytest.mark.parametrize('cross_browser', [(360, 800), (412, 915), (390, 844)], indirect=True)
def test_github_mobile(cross_browser):
    browser.open('https://github.com/')
    signup_mobile()

    browser.quit()
