#Feature: Friends_Module
#
#  Background: Common Steps
#    Given Open the browser and enter the valid url
#
#
#  Scenario Outline: User should able to search and add friends in the application successfully
#    When Enter the Username"<username_>"
#    And Enter the Password"<pwd>"
#    Then Click on login button
#    Examples:
#      | username_                   | pwd        |
#      | jadhavsanjana1975@gmail.com | Cartoon#98 |
#
#  Scenario: Verify that user is able to Click on friend button and able to confirm the friend request
#    When Enter the Username"jadhavsanjana1975@gmail.com"
#    And Enter the Password"Cartoon#98"
#    And Click on login button
#    And Click on friends button
#    Then Click on friend request button
#
#
#  Scenario: Verify that user is able to click on suggestion button
#    When Enter the Username"jadhavsanjana1975@gmail.com"
#    And Enter the Password"Cartoon#98"
#    And Click on login button
#    And Click on friends button
#    Then Click on suggestion button



