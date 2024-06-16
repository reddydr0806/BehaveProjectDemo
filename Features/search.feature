Feature: Search Functionality

  Scenario: Search for valid product
    Given I got navigated to home page0
    When I enter the Product number
    And I click on Search Button
    Then Valid product details should be visible


  Scenario: Search for Invalid Product
    Given I got navigated to homepage
    When I enter the invalid product name/number
    And I click on Search Button
    Then proper message should be displayed

  Scenario: Search for any product without entering any product
    Given I got navigated to homepage
    When I don't enter the product name/number
    And I click on Search Button
    Then proper message should be displayed
