"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

from selene import browser

from pages.home_page import signup_desktop, signup_mobile


def test_github_desktop(desktop_browser):
    browser.open('https://github.com/')
    signup_desktop()


def test_github_mobile(mobile_browser):
    browser.open('https://github.com/')
    signup_mobile()
