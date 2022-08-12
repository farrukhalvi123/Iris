Feature: This is to test iris app login functionality
Background:
Given Launch the browser
When Open the iris URL



Scenario Outline: Test Login Functionality
Then I Login with <email> and <password>
Then Verify we are on the View Page or Show error
Then Close the browser

Examples:
|email | password |
| ngushashaguy@chevron.com | Benue83!! |
| ngusha@chevron.com | AAAAABBBcCc |
# | ngusha1@chveron.com | empty |
#| empty | Demo1234 |
# | empty | empty |