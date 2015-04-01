require 'frank-cucumber/core_frank_steps.rb'
def app_path
  ENV['APP_BUNDLE_PATH'] || (defined?(APP_BUNDLE_PATH) && APP_BUNDLE_PATH)
end

Given /^I launch the app$/ do
  # latest sdk and iphone by default
  launch_app app_path
end

Given /^I launch the app$/ do
    sdk = ENV['FRANK_SDK']
    
    idiom = ENV['FRANK_IDIOM'] || 'ipad'
    
    launch_app( app_path, sdk, idiom )
end

Given(/^I launch the app$/) do
    launch_app_in_simulator
    wait_for_frank_to_come_up
    then(/^I should be on the Login screen$/) do
        view_with_mark_exists("Login")
    end
end
When(/^I log in with a valid userid and password$/) do
    fill_in 'Enter a Username', :with => 'billalkohistani@gmail.com'
    fill_in 'Enter a Password', :with => 'billal'
    touch "button marked:'login'"
    then(/^I am on the start view$/) do
        view_with_mark_exists("Profile")
    end
end

When(/^I touch the food list button$/ )
    touch "button marked:'Food List'"
    then(/^I shoud see foods$/) do
        view_with_mark_exists("Snack")
    end
end

When(/^I touch the @Me button$/ )
    touch "button marked:'Profile'"
    then(/^I should see Profile$/)
        view_with_mark_exists("Profile")
    end

end
Given(/^I am on the Profile page)
    view_with_mark_exists("Logout")
    When(/^I touch the logout button$/)
        touch "button marked:'Logout'"
    end
    then(/^I should see login page)
        view_with_mark_exists("Login")
    end
end
When /^I quit the simulator/ do
    quit_simulator
end
When /^I reset the simulator/ do
    simulator_reset_data
end