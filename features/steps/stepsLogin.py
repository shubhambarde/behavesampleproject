from behave import given, when, then

@given("user starts the browser")
def step_impl(context):
    print("Given user starts the browser")

@when("user enters the application URL")
def step_impl(context):
    print("When user enters the application URL")

@when("user enters the valid login credentials")
def step_impl(context):
    print("user enters the valid login credentials")

@then("user should navigate to Home Page")
def step_impl(context):
    print("Then user should navigate to Home Page")