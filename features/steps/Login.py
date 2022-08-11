from behave import *



@then("We Login to the iris website")
def step_impl(context):
    context.enter_email("ngushashaguy@chevron.com")
    context.enter_password("Benue83!!")
    context.click_login()
    raise NotImplementedError(u'STEP: Then We Login to the iris website')


@then("Verify we are on the View Page")
def step_impl(context):
   assert "View" in context.driver.page_source()