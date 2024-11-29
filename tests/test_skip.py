"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser

from pages.home_page import signup_desktop, signup_mobile


def test_github_desktop(cross_browser):
    if cross_browser == 'mobile':
        pytest.skip('Run only on desktops')
    browser.open('https://github.com/')
    signup_desktop()

    browser.quit()


def test_github_mobile(cross_browser):
    if cross_browser == 'desktop':
        pytest.skip('Run only on mobile')
    browser.open('https://github.com/')
    signup_mobile()

    browser.quit()
