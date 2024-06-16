
Feature: Login to Orange HRM Application


  Scenario: User should be able to login to Orange HRM Application with correct credentials
    Given User has opened the Orange HRM Application Page
    When User enters the Username
    And User enters the Password
    And User clicks on the Login Button
    Then User should be successfully navigated to Account Homepage



