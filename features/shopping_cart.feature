Feature: Verify the shopping cart and wishlist functionality
  Background: Given the user is on the home page


  Scenario: Verify that the user can add items in the cart without being logged in
    When The user clicks on the "ADAUGA IN COS" button under any item
    Then The item is added to the user's cart and the item count increased by one


  Scenario: Verify that the user can add items to the wishlist without being logged in
    When The user clicks on the heart button under any item
    Then The item is added to the user's wishlist and the item count increased by one


  Scenario: Verify that the user can remove items from the cart without being logged in
    When The user has at least one item into the shopping cart
    When The user clicks on "COSUL MEU" button to view the items in the cart
    When The user clicks to remove an item from the shopping cart
    Then The the item has been removed from the user's cart


  Scenario: Verify that the user can remove items from the wishlist without being logged in
    When The user has at least one item into the wishlist
    When The user clicks on "Wishlist" button to view the items in the cart
    When The user clicks to remove an item from the wishlist
    Then The the item has been removed from the user's wishlist


  Scenario: Verify that the items added to the cart are saved on the user's account
    When The user successfully logs into the account
    #dupe
    When The user clicks on the 'ADAUGA IN COS' button under any item
    When The user relogs into the account
    Then The item added before relog has been saved into the shopping cart and is visible

  Scenario: Verify that the items added to the wishlist are saved on the user's account
    #dupe
    When The user successfully logs into the account
    #dupe
    When The user clicks on the 'ADAUGA IN COS' button under any item
    #dupe
    When The user relogs into the account
    Then The item added before relog has been saved into the wishlist and is visible
