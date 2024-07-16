# Created by franc at 16/7/2024
Feature: OrangeHRM Logo

  Scenario: Logo presence on OrangeHRM home page
    Given launch chore browser
    When open orange hrm homepage
    Then verify that the logo present on page
    And Close browser