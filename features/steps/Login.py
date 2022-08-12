import time

from behave import *



@then("I Login with {email} and {password}")
def step_impl(context, email, password):
    time.sleep(3)
    context.loginpage.enter_email(email)
    context.loginpage.enter_password(password)
    context.loginpage.click_login()
    time.sleep(10)



@then("Verify we are on the View Page or Show error")
def step_impl(context):
    try:
        assert "view" in context.driver.page_source
    except:
        assert "WRONG EMAIL" in context.driver.page_source

