Feature: Login flytoday site
  Background:
    Given open the site
    When click on the login link
  @browser
  Scenario Outline: valid login by valid username and password
    Then insert correct username "<username>"
    And insert correct password "<password>"
    And click the login button
    And assertion login by "<username>"
    Examples:
      | username | password |
      | bahram   | 123      |
      | farzan   | 12345    |
#      | bahram   | 777      |
#      | lily     | 123456   |