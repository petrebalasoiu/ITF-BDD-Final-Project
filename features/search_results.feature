Feature: Verify that the search results are displayed and can be filtered
  Background:
    Given the user has searched for an item


  Scenario: Verify that first page displayed contains 30 items
    When the user clicks to search
    Then the first page displayed contains 30 items


  Scenario: Verify that the filter displays only the item type selected
    When the user clicks on a certain item type to be filtered
    Then the page displays only filtered items


  Scenario: Verify that the items can be sorted in ascending order
    When the user clicks on the sort dropdown
    When the user selects the ascending order
    Then the page displays the items from the lowest to the highest price

  Scenario: Verify that the items can be sorted in descending order
    When the user clicks on the sort dropdown
    When the user selects the descending order
    Then the page displays the items from the highest to the lowest price

  Scenario: Verify that the filters can be reset
    When the user clicks on the filter reset button
    Then all the filters are removed and the page refreshes with the original search