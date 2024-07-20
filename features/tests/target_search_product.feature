Feature: Target product search tests


#  Scenario: User can search for product
#    Given Open Target main page
#    When Search for xbox
#    Then Verify search results for xbox


  Scenario: User can search for product
    Given Open Target main page
    When Search for xbox
    Then Verify all products have product name and product picture
