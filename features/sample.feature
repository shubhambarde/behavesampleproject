Feature: Login

    Scenario: Verify Login using correct credentials
        Given user starts the browser 
        When user enters the application URL
        and user enters the valid login credentials
        Then user should navigate to Home Page
    
