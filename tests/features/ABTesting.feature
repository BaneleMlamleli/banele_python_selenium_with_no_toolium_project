@ABTesting
Feature: AB Test Variation 1

    Background: landing page
        Given a user is on the website home page

    Scenario: AB Test Variation 1
        When user clicks on "A/B Testing"
        Then user is redirected to the AB Test Variation 1 page