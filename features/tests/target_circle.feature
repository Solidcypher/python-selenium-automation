Feature: Tests for Target Circle UI


  Scenario: Verify Target Circle has correct number of benefit cells
    Given Open Target main page
    When Click on Target Circle link
    Then Verify circle page has 10 benefit cells
