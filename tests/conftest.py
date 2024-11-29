import pytest
from selene import browser


@pytest.fixture(scope='function', params=[(360, 800), (412, 915), (390, 844),
                                          (1920, 1080), (1366, 768)])
def cross_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width > 1000:
        return 'desktop'
    else:
        return 'mobile'


@pytest.fixture(scope='function', params=[(1920, 1080), (1366, 768)])
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[(360, 800), (412, 915), (390, 844)])
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield

    browser.quit()
