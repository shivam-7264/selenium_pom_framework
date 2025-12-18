from pages.login_page import LoginPage

def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)

    login_page.open("https://www.orangehrm.com/")
    login_page.fill_contact_form("Shivam Pratap Singh")

    assert "Human Resources Management Software | HRMS | OrangeHRM" in driver.title
