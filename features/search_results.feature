@F2 @SearchResults
Feature: Verify that the search results are displayed and can be filtered
  Background:
    Given the user is on the homepage and has searched for an item

  @T8 @UI @itemCount
  Scenario: Verify that first page displayed contains 30 items
    Then the first page displayed contains 30 items

  @T9 @UI @filter @itemType
  Scenario: Verify that the filter displays only the item type selected
    When the user clicks on a certain item type to be filtered
    Then the page displays only filtered items

  @T10 @UI @sorting @ascendingOrder
  Scenario: Verify that the items can be sorted in ascending order
    When the user selects the ascending order from the dropdown menu
    Then the page displays the items from the lowest to the highest price

  @T11 @UI @sorting @descendingOrder
  Scenario: Verify that the items can be sorted in descending order
    When the user selects the descending order from the dropdown menu
    Then the page displays the items from the highest to the lowest price

  @T12 @UI @filter @reset
  Scenario: Verify that the filters can be reset
    When the user clicks on a certain item type to be filtered
    When the user clicks on the filter reset button
    Then all the filters are removed and the page refreshes with the original search
