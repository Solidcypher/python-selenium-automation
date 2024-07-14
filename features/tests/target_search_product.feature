Feature: Target product search tests


  Scenario: User can search for product
    Given Open Target main page
    When Search for xbox
    Then Verify search results for xbox