
Feature: Target empty cart tests


  Scenario: User can see empty cart text
    Given Open Target main page
    When Click on cart icon
    Then Verify empty cart text appears