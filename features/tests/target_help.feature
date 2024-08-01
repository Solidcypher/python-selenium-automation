Feature: Tests for Target Help UI


#  Scenario: Verify that Target Help has all UI elements
#    Given Open Target help page
#    Then Verify Help page has all 6 UI elements

  Scenario: User can select Delivery and Pickup from Browse Help dropdown menu
    Given Open Target Help Returns page
    Then Verify Returns page opened
    When Select Delivery & Pickup in dropdown menu
    Then Verify Drive Up & Order Pickup page opened