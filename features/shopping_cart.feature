Feature: Verify the shopping cart and wishlist functionality
  Background:
    Given the user has searched for a band name

  @T13 @UI @cart @addItem
  Scenario: Verify that the user can add items in the cart
    When the user clicks to add one item into the cart
    When the user clicks view the cart
    Then the item has been added to the user's cart

  @T14 @UI @cart @removeItem
  Scenario: Verify that the user can remove items from the cart
    When the user clicks view the cart
    When the user clicks to remove the item from the shopping cart
    Then the item has been removed from the user's cart

  @T15 @UI @wishlist @addItem
  Scenario: Verify that the user can add items to the wishlist
    When the user clicks to add one item to the Wishlist
    When the user clicks to view the Wishlist
    Then the item has been added to the user's Wishlist

  @T16 @UI @wishlist @removeItem
  Scenario: Verify that the user can remove items from the wishlist without being logged in
    When the user clicks to view the Wishlist
    When the user clicks to remove the item from the Wishlist
    Then the item has been removed from the user's Wishlist
