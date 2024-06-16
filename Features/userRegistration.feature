Feature: New User Registration to Sign Up to the application

  @completed
  Scenario: Register the New User details to Sign-Up
    Given I launched the Application website
    When I click on MyAccount-Register option
    And Fill all all details
    And Check the Policy Checkbox
    And Click on Continue button
    Then I navigated to My Account Dashboard HomePage