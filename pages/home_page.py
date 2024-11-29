from selene import browser

signup_button = browser.element('.HeaderMenu-link--sign-up')


def signup_desktop():
    signup_button.click()


def signup_mobile():
    browser.element('.Button-content').click()
    signup_button.click()
