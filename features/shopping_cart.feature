Feature: Verify the shopping cart and wishlist functionality
  Background:
    Given the user has searched for a band name


  Scenario: Verify that the user can add items in the cart
    When the user clicks to add one item into the cart
    When the user clicks view the cart
    Then the item has been added to the user's cart


  Scenario: Verify that the user can remove items from the cart
    When the user clicks view the cart
    When the user clicks to remove the item from the shopping cart
    Then the item has been removed from the user's cart


  Scenario: Verify that the user can add items to the wishlist
    When the user clicks to add one item to the Wishlist
    When the user clicks to view the Wishlist
    Then the item has been added to the user's Wishlist


  Scenario: Verify that the user can remove items from the wishlist without being logged in
    When the user clicks to view the Wishlist
    When the user clicks to remove the item from the Wishlist
    Then the item has been removed from the user's Wishlist



