@F4 @UserAccount
Feature: Verify the user login functionality
  Background:
    Given the user is on the login page

  @17 @UI @login @validCredentials
  Scenario Outline: Verify that the user can log in when inserting valid credentials
    When the user inserts username "<username>" and password "<password>"
    When the user clicks on the login button
    Then the user is successfully logged into the account
    Examples:
      | username   | password |  |
      | test.user1 | test     |  |
      | test.user2 | test     |  |
      | test.user3 | test     |  |

  @18 @UI @login @invalidCredentials
  Scenario Outline: Verify that the user cannot log in and is prompted with an error when inserting invalid credentials
    When the user inserts username "<username>" and password "<password>"
    When the user clicks on the login button
    Then the user is prompted with the "<error_message>" and cannot log into the application
    Examples:
      | username          | password          | error_message     |
      | test.user1        | invalid_password  | Invalid password  |
      | invalid_username  | test              | Invalid username  |

  @19 @UI @login @missingPassword
  Scenario: Verify that the user cannot log in and is prompted with an error when inserting only the username
    When the user inserts only the username and not the password
    When the user clicks on the login button
    Then the user is prompted with the "Invalid password" and cannot log into the application

  @20 @UI @login @missingUsername
  Scenario: Verify that the user cannot log in and is prompted with an error when inserting only the password
    When the user inserts only the password and not the username
    When the user clicks on the login button
    Then the user is prompted with the "Invalid username" error and cannot log into the application
