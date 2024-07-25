
Feature: Target signin tests


#  Scenario: User can navigate to signin form
#    Given Open Target main page
#    When Click on sign in icon
#    When Click on sign in on side navigation
#    Then Verify sign in page appears

  Scenario: User can login to Target from login page
    Given Open Target main page
    When Click on sign in icon
    When Click on sign in on side navigation
    When Input email address
    When Input password
    When Click sign in
    Then Verify user is logged in