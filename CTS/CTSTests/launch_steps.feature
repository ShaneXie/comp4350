Feature:
    I want to log in to the app using my username
    So that I can access the system with my own account

Scenario: Successful login
Given I launch the app
When I log in with a valid userid and password
Then I am on the start view

Feature:
    I want to touch the food list button so that I can navigate
    and see the food list
Scenario: View List
When I touch the Food List Button
Then I am on the food List
Then I should see a food item

Feature:
    I want to touch the BMI button so that I can navigate
    and see the BMI
Scenario: View BMI
When I touch the Me Button
Then I am on the BMI page

Feature:
    I want to touch the @Me button so that I can navigate
    and see the Profile
Scenario: View Profile
When I touch the @Me Button
Then I am on the Profile page

Feature:
    I want to log out of the app by pressing the button
    So that I can successfully log out
Scenario: Successful logout
Given I launch I press logout
Then I am in the login screen