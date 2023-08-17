@AddAndRemoveElement
Feature: Add and remove an element

    Background: landing page
        Given a user is on the website home page

    Scenario: Add and remove an element
        When user clicks on "Add/Remove Elements"
        When user clicks on Add Element button
        Then button Delete is displayed
        Then user clicks on the button Delete