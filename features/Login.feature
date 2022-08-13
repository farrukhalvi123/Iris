Feature: This is to test iris app login functionality
Background:
Given Launch the browser
When Open the iris URL


Scenario: Test Login Functionality (Valid Data)
Then I Login with ngushashaguy@chevron.com and Benue83!!
Then Verify we are on the View Page or Show error
Then Close the browser


Scenario Outline: Test Login Functionality
Then I Login with <email> and <password>
Then Verify we are on the View Page or Show error
Then Close the browser

Examples:
|email | password |
| ngusha@chevron.com | AAAAABBBcCc |
| ngusha1 | AAAAABBBcCc |
#| empty | Demo1234 |
# | empty | empty |