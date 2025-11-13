Feature: E2E test app

    Example: check that caroussel displayed
        Given the user launchs the app
        When the user is on the carrousel
        And the user handles the carrousel
        Then the user is on the app

    Example: check that user can find lydia city page
        Given the user is on the homepage of the app
        When the user searches for Lydia city
        Then the Lydia page is displayed
    
    Example: check that user can set language to french
        Given the user is on the lydia city page
        When the user changes the app language to french
        Then the lydia page is displayed in french
    
    Example: check that user can open cresus section
        Given the user is on the lydia city page in french
        When the user scrolls to the Cresus section
        And the user clicks on the Cresus section
        Then the Cresus page is displayed