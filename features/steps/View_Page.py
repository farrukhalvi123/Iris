from behave import *




@step("I am able to select the pagination dropdown")
def step_impl(context):
    context.view.pagination_click_50()

@then("the field should show the value selected")
def step_impl(context):
   assert "1 – 50 " in context.driver.page_source
