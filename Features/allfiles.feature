Feature: OrangeHRM Logo

  Scenario: Logo presence on OrangeHRM Login Page
    Given Launch Chrome Browser
    When open Orange HRM page
    Then verify that Logo is present
    And close the browser
