Feature: Target cart tests


  Scenario: User can see empty cart text
    Given Open Target main page
    When Click on cart icon
    Then Verify empty cart text appears

#  Scenario: User can add product to cart
#    Given Open Target main page
#    When Search for tea
#    When Click add to cart on search page
#    When Click pickup add to cart
#    When Click on close X
#    When Click on cart icon
#    Then Verify 1 item(s) in cart

