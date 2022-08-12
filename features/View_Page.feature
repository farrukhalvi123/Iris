# Created by nswv at 8/12/2022

Feature: As a facilitator I will like to search assets, expand assets to view content
      and perform pagination to view more content.

Background:
Given Launch the browser
When Open the iris URL
Then I Login with ngushashaguy@chevron.com and Benue83!!

  Scenario: As a facilitator I would like to use pagination to view 50 items on the page
    And I am able to select the pagination dropdown
    Then the field should show the value selected

  Scenario: As a facilitator I would like to use pagination to view 100 items on the page
    And I am able to select the pagination dropdown
    Then the field should show the value selected