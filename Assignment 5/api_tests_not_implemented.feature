Feature: Applicant Edge Case Handling

  Scenario: Create applicant with invalid date format
    Given I am an authenticated user
    When I submit an applicant with a malformed date of birth
    Then the system should return a 400 BAD REQUEST response

  Scenario: Retrieve non-existent applicant
    Given I am an authenticated user
    When I request an applicant ID that does not exist
    Then the system should return a 404 NOT FOUND response

  Scenario: Partially update applicant using PATCH
    Given I am an authenticated user
    And an applicant exists
    When I send a PATCH request with partial data
    Then the system should return a 200 OK response

  Scenario: Create duplicate applicant
    Given I am an authenticated user
    And an identical applicant already exists
    When I submit a request with the same name and DoB
    Then the system should return a 409 CONFLICT response or allow duplication per business rules

  Scenario: Create applicant with excessive name length
    Given I am an authenticated user
    When I submit an applicant with a name over 255 characters
    Then the system should return a 400 BAD REQUEST response


Feature: Address Input Validation

  Scenario: Create address with invalid ZIP format
    Given I am an authenticated user
    When I submit an address with a non-numeric ZIP code
    Then the system should return a 400 BAD REQUEST response

  Scenario: Create address with invalid OwnerType
    Given I am an authenticated user
    When I submit an address with an unrecognized OwnerType value
    Then the system should return a 400 BAD REQUEST response

  Scenario: Delete non-existent address
    Given I am an authenticated user
    When I delete an address using an invalid ID
    Then the system should return a 404 NOT FOUND response

  Scenario: Submit address with missing required fields
    Given I am an authenticated user
    When I omit mandatory address fields like City or State
    Then the system should return a 400 BAD REQUEST response

  Scenario: Access address detail with invalid ID format
    Given I am an authenticated user
    When I retrieve an address using a non-integer ID
    Then the system should return a 400 BAD REQUEST response


Feature: Contact Input Handling

  Scenario: Create contact with invalid phone number
    Given I am an authenticated user
    When I submit a contact with an incorrectly formatted phone number
    Then the system should return a 400 BAD REQUEST response

  Scenario: Submit contact without relationship
    Given I am an authenticated user
    When I submit a contact without specifying relationship
    Then the system should return a 400 BAD REQUEST response

  Scenario: Retrieve non-existent contact
    Given I am an authenticated user
    When I request a contact by a non-existent ID
    Then the system should return a 404 NOT FOUND response

  Scenario: Partially update contact using PATCH
    Given I am an authenticated user
    And a contact exists
    When I send a PATCH request with updated phone number
    Then the system should return a 200 OK response

  Scenario: Submit numeric value for contact's name
    Given I am an authenticated user
    When I submit a numeric value for First_Name
    Then the system should return a 400 BAD REQUEST response


Feature: Admin Access Edge Cases

  Scenario: Admin deletes a user via API
    Given I am logged in as a superuser
    When I send a DELETE request for a user
    Then the system should return a 204 NO CONTENT response

  Scenario: Non-admin attempts to delete a user
    Given I am logged in as a regular user
    When I attempt to delete another user via API
    Then the system should return a 403 FORBIDDEN response

  Scenario: Admin assigns user to a group
    Given I am logged in as a superuser
    When I update a user's group membership via API
    Then the system should return a 200 OK response

  Scenario: Login fails with incorrect credentials
    Given I am an anonymous user
    When I try to log in with an incorrect username or password
    Then the system should return a 401 UNAUTHORIZED response

  Scenario: Access admin panel without authentication
    Given I am not logged in
    When I try to access the admin dashboard
    Then the system should redirect me to the login page
