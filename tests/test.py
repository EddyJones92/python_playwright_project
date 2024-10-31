from playwright.sync_api import expect


def test_login(login):
    login.go_to_login_page()
    login.login(login.login_name, login.password)
    greeting = login.get_greeting()
    expect(greeting).to_have_text("Hello, alice")


def test_error_login_with_wrong_name(login):
    error_text = 'Your username and password didn\'t match. Please try again.'
    incorrect_name = 'Eddy'
    login.go_to_login_page()
    login.login(incorrect_name, login.password)
    error = login.get_error_text()
    expect(error).to_have_text(error_text)


def test_error_login_with_wrong_password(login):
    error_text = 'Your username and password didn\'t match. Please try again.'
    password = '123456'
    login.go_to_login_page()
    login.login(login.login_name, password)
    error = login.get_error_text()
    expect(error).to_have_text(error_text)


def test_dont_have_account_button(login, base):
    login.go_to_login_page()
    login.go_to_register_page()
    base.check_current_url('register')




