
Feature: Target signin tests


#  Scenario: User can navigate to signin form
#    Given Open Target main page
#    When Click on sign in icon
#    When Click on sign in on side navigation
#    Then Verify sign in page appears

#  Scenario: User can login to Target from login page
#    Given Open Target main page
#    When Click on sign in icon
#    When Click on sign in on side navigation
#    When Input email address
#    When Input password
#    When Click sign in
#    Then Verify user is logged in

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target main page
    When Click on sign in icon
    And Click on sign in on side navigation
    And Store original window
    And Click Terms and Conditions link
    And Switch to newly opened window
    Then Verify Terms and Conditions page is open
    And User can close current page
    And User can return to original window
