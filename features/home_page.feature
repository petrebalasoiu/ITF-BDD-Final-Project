Feature: Verify the home page elements
  Background:
    Given the user is on the home page


  Scenario: Verify that the website's title is matching
    Then the home page title matches


  Scenario: Verify that the logo button is redirecting to the home page
    When the user clicks on the logo button
    Then the user is redirected to the home page


  Scenario: Verify that the "Home" button is redirecting to the home page
    When the user clicks on the "Home" button
    Then the user is redirected to the home page


  Scenario: Verify that the "Produse noi" button is redirecting to the "Produse noi" page
    When the user clicks on the "Produse noi" button
    Then the user is redirected to the "Produse noi" page


  Scenario: Verify that the "Producatori" button is loading the "Producatori" page
    When the user clicks on the "Producatori" button
    Then the user is redirected to the "Producatori" page


  Scenario: Verify that the "Contact" button is loading the "Contact" page
    When the user clicks on the "Contact" button
    Then the user is redirected to the "Contact" page


  Scenario: Verify that the search functionality is working as intended
    When the user types a product name in the search bar
    When the user clicks to confirm the search
    Then the items matching the search are presented to the user and displayed in the page source