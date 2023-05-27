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


  # ------------------- SOON TO BE IMPLEMENTED -------------------
#  Scenario: Verify that the items added to the cart are saved on the user's account
#    When The user successfully logs into the account
#    #dupe
#    When The user clicks on the 'ADAUGA IN COS' button under any item
#    When The user relogs into the account
#    Then The item added before relog has been saved into the shopping cart and is visible
#
#  Scenario: Verify that the items added to the wishlist are saved on the user's account
#    #dupe
#    When The user successfully logs into the account
#    #dupe
#    When The user clicks on the 'ADAUGA IN COS' button under any item
#    #dupe
#    When The user relogs into the account
#    Then The item added before relog has been saved into the wishlist and is visible
