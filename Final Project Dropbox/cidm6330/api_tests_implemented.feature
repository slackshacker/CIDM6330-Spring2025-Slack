Feature: Applicant Management

  Scenario: Create a valid applicant
    Given I am an authenticated user
    When I submit a valid applicant creation request
    Then the system should return a 201 CREATED response

  Scenario: Create applicant with missing field
    Given I am an authenticated user
    When I submit an applicant request with missing required fields
    Then the system should return a 400 BAD REQUEST response

  Scenario: Retrieve an existing applicant
    Given I am an authenticated user
    And an applicant exists
    When I retrieve the applicant by ID
    Then the system should return a 200 OK response with applicant details

  Scenario: Update an existing applicant
    Given I am an authenticated user
    And an applicant exists
    When I submit a full update with valid data
    Then the system should return a 200 OK response

  Scenario: Delete an applicant
    Given I am an authenticated user
    And an applicant exists
    When I send a delete request for the applicant
    Then the system should return a 204 NO CONTENT response


Feature: Address Management

  Scenario: Create a valid address
    Given I am an authenticated user
    And an applicant exists
    When I submit a valid address creation request
    Then the system should return a 201 CREATED response

  Scenario: Retrieve the list of addresses
    Given I am an authenticated user
    When I retrieve the list of addresses
    Then the system should return a 200 OK response with address data

  Scenario: Update an existing address
    Given I am an authenticated user
    And an address exists
    When I submit a full update to the address
    Then the system should return a 200 OK response

  Scenario: Delete an address
    Given I am an authenticated user
    And an address exists
    When I send a delete request for the address
    Then the system should return a 204 NO CONTENT response


Feature: Contact Management

  Scenario: Create a valid contact
    Given I am an authenticated user
    When I submit a valid contact creation request
    Then the system should return a 201 CREATED response

  Scenario: Retrieve a contact by ID
    Given I am an authenticated user
    And a contact exists
    When I retrieve the contact by ID
    Then the system should return a 200 OK response

  Scenario: Update an existing contact
    Given I am an authenticated user
    And a contact exists
    When I submit a full update to the contact
    Then the system should return a 200 OK response

  Scenario: Delete a contact
    Given I am an authenticated user
    And a contact exists
    When I send a delete request for the contact
    Then the system should return a 204 NO CONTENT response


Feature: Admin Access Control

  Scenario: Non-admin cannot access admin panel
    Given I am logged in as a non-admin user
    When I try to access the Django admin panel
    Then the system should redirect or deny access

  Scenario: Admin can access admin panel
    Given I am logged in as a superuser
    When I access the Django admin panel
    Then the system should return a 200 OK response

  Scenario: Non-admin cannot create a user via API
    Given I am logged in as a non-admin user
    When I send a request to create a new user
    Then the system should return a 403 FORBIDDEN or 401 UNAUTHORIZED

  Scenario: Admin can create a user via API
    Given I am logged in as a superuser
    When I send a request to create a new user
    Then the system should return a 201 CREATED response
