from behave import given, when, then

def before_all(context):
    print("Before all tests")
    

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
    inputENV = context.config.userdata.get("ENV")
    print("Environment: {inputENV}")
    if inputENV == "sys":
        context.baseURL = "https://www.sys.com"
    elif inputENV == "dev": 
        context.baseURL = "https://www.dev.com" 
    elif inputENV == "prod":
        context.baseURL = "https://www.prod.com"
    print(context.baseURL)
    # url = context.baseURL
    # print(url)

@then("user should not navigate to Home Page")
def step_impl(context):
    print("Then user should not navigate to Home Page")
    # url = context.baseURL
    # print(url)
    inputENV = context.config.userdata.get("ENV")
    print("Environment: {inputENV}")
    if inputENV == "sys":
        context.baseURL = "https://www.sys.com"
    elif inputENV == "dev": 
        context.baseURL = "https://www.dev.com" 
    elif inputENV == "prod":
        context.baseURL = "https://www.prod.com"
    print(context.baseURL)
    print(f"connecting to" f"{context.baseURL} with {inputENV} environment")