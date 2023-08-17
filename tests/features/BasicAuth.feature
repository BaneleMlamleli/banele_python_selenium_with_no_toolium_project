@BasicAuth
Feature: Login using a JavaScript Alert popup windows authentication

    Background: landing page
        Given a user is on the website home page

    Scenario Outline: Enter correct and incorrect login credentials for authentication
        When user clicks on "Basic Auth"
        Then user enter "<username>" and "<password>" and clicks on sign in button
        Then login status
        Examples:
            | username | password |
            | admin    | admin    |
# | wrong_pw | wrong_usernm |