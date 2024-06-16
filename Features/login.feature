Feature: Login to Website

  @done
  Scenario: Login to website with valid creds
    Given I launched the website
    When I navigate to My Account tab & click on Login button
    And I enter email id
    And I enter password
    And I click on Login submit button
    Then  I should be logged in to website


