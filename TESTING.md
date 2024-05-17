<h1 align="center">Little Explorers-Testing</h1>

![Little Explorers on different screens]()

[View the live website here - Little Explorers](https://little-explorers-c2ba86cc535f.herokuapp.com/)

---

<h2>Contents</h2


<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Introduction

Testing is essential to ensure that the website functions properly, free from bugs, and that users can fully utilise its features before its release to the general market. This guarantees a positive user experience (UX) and encourages repeat visits from players.

Throughout the game development process, I relied on Chrome developer tools to assess page responsiveness across various screen sizes and address any encountered issues.

In troubleshooting, I utilised the console to log and monitor JavaScript code, aiding in resolving aspects of the game that did not perform as intended. All the test results detailed below are based on the [deployed site](https://little-explorers-c2ba86cc535f.herokuapp.com/).

---

# Automated Testing

## HTML Validation

[W3C](https://validator.w3.org/) was used to validate the HTML.

Minor code structure errors were addressed (such a extra closing div's) and invalid form describers were removed (e.g duplicate required elements, or required on elements hidden from the user).

Please note that the error messages which relate to a "Trailing slash on void elements" have been filtered as they are automatically added by the browser and are not a true error (as advised by the CI tutors).

As all validated screens look the same I am just displaying one here with the individual valid test results documented in the table below. ![HTML validation](documentation/testing/images/validation/html-valid-example.PNG)


<details><summary>HTML Validation Results Table</summary>

| **Page (html)**      | **Result**                            |
|----------------------|---------------------------------------|
| Add Holiday Types    | Passed- No errors or warnings to show |
| Add Recommendation   | Passed- No errors or warnings to show |
| Base                 | Passed- No errors or warnings to show |
| Contact              | Passed- No errors or warnings to show |
| Create Account       | Passed- No errors or warnings to show |
| Edit Holiday Types   | Passed- No errors or warnings to show |
| Edit Recommendation  | Passed- No errors or warnings to show |
| Holiday Types        | Passed- No errors or warnings to show |
| Index (Home)         | Passed- No errors or warnings to show |
| Profile              | Passed- No errors or warnings to show |
| Recommendations      | Passed- No errors or warnings to show |
| Sign In              | Passed- No errors or warnings to show |
| Users                | Passed- No errors or warnings to show |
| View Recommendations | Passed- No errors or warnings to show |
| 404 Error            | Passed- No errors or warnings to show |

</details>

## CSS Validation
CSS was validated using [W3C Jigsaw](https://jigsaw.w3.org/css-validator/).

<details><summary>CSS Validation Screenshot</summary>
<img src="documentation/testing/images/validation/valid_css.png">
</details>

## Javascript Validation

The JavaScript code was validated using [JSHint](https://jshint.com/). 

Please note, warnings relate the use of ES6/8 and are acceptable for the parameters of this project.

<details><summary>addRecommendation JS</summary>
<img src="documentation/testing/images/validation/javascript-add-recommendation.PNG">
1. Documented an "unsued" function CheckMaxLength. This is triggered from the HTML form.
</details>

<details><summary>createAccount JS</summary>
<img src="documentation/testing/images/validation/javascript-create-account.PNG">
1. Documented an "unsued" function checkPasswordMatch. This is triggered from the HTML form.
</details>

<details><summary>maps-search JS</summary>
<img src="documentation/testing/images/validation/javascript-maps-search.PNG">
1. Documented undefined/unused variables - all are called elsewhere by Google Maps API.
</details>

<details><summary>maps-view JS</summary>
<img src="documentation/testing/images/validation/javascript-maps-view.PNG">
1. Documented undefined/unused variables - all are called elsewhere by Google Maps API.
</details>

<details><summary>maps JS</summary>
<img src="documentation/testing/images/validation/javascript-maps.PNG">
1. Documented undefined/unused variables - all are called elsewhere by Google Maps API.
2. Warnings relating to missing semi colons. All fixed. 
3. One variable unused (address) so removed. 
</details>

<details><summary>script JS</summary>
<img src="documentation/testing/images/validation/javascript-script.PNG">
1. Documented undefined/unused variables - all are called elsewhere by Materialize elements.
2. Warnings relating to missing semi colons. All fixed.  
</details>

<details><summary>sendEmail JS</summary>
<img src="documentation/testing/images/validation/javascript-sendEmail.PNG">
1. Documented undefined/unused variables - all are called elsewhere by emailJS in the contact form. 
</details>

## Python Validation

Python pep8 validation was done via [Code Institute's Python Linter](https://pep8ci.herokuapp.com/).


<details><summary>__init__ Python</summary>
<img src="documentation/testing/images/validation/python-init.PNG">
1. Resolved issues included correcting gaps and whitespace. The import of routes has been left at the bottom of the file. Although this doesn't comply with PEP8, it is necessary to prevent a circular import.
</details>

<details><summary>Models Python</summary>
<img src="documentation/testing/images/validation/python-init.PNG">
1. Resolved issues included correcting gaps/whitespace and retructuring to reduce line length. 
</details>

<details><summary>Routes Python</summary>
<img src="documentation/testing/images/validation/python-routes.PNG">
1. Resolved issues included correcting gaps/whitespace and retructuring to reduce line length.
</details>

## Accessibility

The site underwent an accessibility check using [Silktide's Accessibility Checker.](https://silktide.com/toolbar/)

Several changes were implemented to enhance accessibility:

1. Contrast improvements were applied to the footer and similarly colored buttons to enhance readability.

2. The exclamation mark ("!") was removed from links that do not lead to new pages, ensuring consistency and clarity.

3. Specific descriptions were added as screen reader-only content to aid users in navigating to specific pages and ensuring they are deleting the correct content.

4. Contrast on orange buttons was adjusted to display black text instead of white, improving visibility.

5. Autocomplete options were added to various elements. 

While most contrast issues were addressed, some persist with elements inherited from Materialize form input components.

## Performance

The site was run through the Google Chrome Developer tool Lighthouse to assess it's performance. The scores for each page are listed below. 

** light house results 

**other content - testing results (manual)


# Manual Testing

The desktop version of the site underwent testing across various browsers and devices to ensure compatibility. Testing included Google Chrome, Mozilla Firefox, and Microsoft Edge on desktop computers. Additionally, Chrome was tested on both Lenovo Tablet and Pixel devices, while Safari was used for mobile testing.

The site was responsive on all browsers and devices (down to  320px as recommended by [Free Code Camp](https://www.freecodecamp.org/news/media-query-css-example-max-and-min-screen-width-for-mobile-responsive-design/))

## Mobile and Desktop Test Results

<details><summary>Nav Bar</summary>

| ****Feature****              | ****Expected Outcome****                     | ****Test Performed**** | ****Result****                                   | ****Pass/Fail**** |
|------------------------------|----------------------------------------------|------------------------|--------------------------------------------------|-------------------|
| All Users                    |                                              |                        |                                                  |                   |
| Little Explorer Logo         | Redirect to Home page when clicked           | Clicked Logo/Title     | Redirects to Home Page                           | Pass              |
| Home Page Link               | Redirect to Home page when clicked           | Clicked Link           | Redirects to Home Page                           | Pass              |
| Holidays Page Link           | Redirect to Holidays page when clicked       | Clicked Link           | Redirects to Holidays Page                       | Pass              |
| Contact Page Link            | Redirect to Contact page when clicked        | Clicked Link           | Redirects to Contact Page                        | Pass              |
| Account Dropdown             | Reveals Links to all users                   | Clicked Account Title  | DropDown menu shown                              | Pass              |
| Create Account Link          | Redirect to Create Account page when clicked | Clicked Link           | Redirects to Create Account Page                 | Pass              |
| Sign In Link                 | Redirect to Sign In Page when clicked        | Clicked Sign In        | Redirected to Sign in Page                       | Pass              |
| Logged In User (not Admin)   |                                              |                        |                                                  |                   |
| Add Holiday Link             | Redirect to Add Holiday page when clicked    | Clicked Link           | Redirects to Add Holiday Page                    | Pass              |
| Account Dropdown             | Reveals Links to all users                   | Clicked Account Title  | DropDown menu shown                              | Pass              |
| Profile Link                 | Redirect to Profile Page when clicked        | Clicked Link           | Redirects to Profile Page                        | Pass              |
| Sign Out Link                | Signs the User out                           | Clicked Sign Out       | Logged out of the system (notified with message) | Pass              |
| Admin only                   |                                              |                        |                                                  |                   |
| Manage (admin only) Dropdown | Reveals links for admin                      | Clicked Manage Title   | DropDown menu shown                              | Pass              |
| Holiday Types Link           | Redirect to Holiday Types page when clicked  | Clicked Link           | Redirects to Holiday Types Page                  | Pass              |
| Users Link                   | Redirect to Users page when clicked          | Clicked Link           | Redirects to Users Page                          | Pass              |
| Add Holiday page             | Redirect to Add Holiday page when clicked    | Clicked Link           | Redirects to Add Holiday Page                    | Pass              |
| Create Account               | Redirect to Create Account page when clicked | Clicked Link           | Redirects to Create Account Page                 | Pass              |         

</details>

<details><summary>Footer</summary>

| **Feature**                  | **Expected Outcome**             | **Test Performed** | **Result**                       | **Pass/Fail** |
|------------------------------|----------------------------------|--------------------|----------------------------------|---------------|
| Question Link                | Navigates to the Contact Pagr    | clicked on link    | Redirected to the Contact Page   | Pass          |
| Question Link Hover          | Changes Clour                    | Hovered over link  | Colour changed                   | Pass          |
| Social Media Icon: X         | Navigates to Twitter home page   | clicked on icon    | Nagivaged to Twitter Home Page   | Pass          |
| Social Media Icon:  Facebook | Navigates to  Facebook home page | clicked on icon    | Nagivaged to  Facebook Home Page | Pass          |
| Social Media Icon: Instagram | Navigates to Instagram home page | clicked on icon    | Nagivaged to Instagram Home Page | Pass          |
| Social Media Icon: Pintrest  | Navigates to Pintrest home page  | clicked on icon    | Nagivaged to Pintrest Home Page  | Pass          |
| Social Media Icon: LinkedIn  | Navigates to LinkedIn home page  | clicked on icon    | Nagivaged to LinkedIn Home Page  | Pass          |
| Social Media Icon Hover      | Changes Clour                    | Hovered over link  | Colour changed                   | Pass          |
 


</details>

<details><summary>Home Page (Index.html)</summary>

| **Feature**                               | **Expected Outcome**                 | **Test Performed**          | **Result**                            | **Pass/Fail** |
|-------------------------------------------|--------------------------------------|-----------------------------|---------------------------------------|---------------|
| All users                                 |                                      |                             |                                       |               |
| Browse Holidays Button                    | Navigates to the Holidays Page       | Clicked Button              | Redirected to the Holidays Page       | Pass          |
| Browse Holidays Button Hover              | Changes Colour                       | Hovered over button         | Changes Colour                        | Pass          |
| Holiday Card Image                        | Navigates to full page reveiw        | Clicked on card image       | Redirected to full page reveiw        | Pass          |
| Holiday Card Image Magnifying glass image | Navigates to full page reveiw        | Clicked on magnifying glass | Redirected to full page reveiw        | Pass          |
| See More holidays Button                  | Navigates to the Holidays Page       | Clicked Button              | Redirected to the Holidays Page       | Pass          |
| See More holidays Button Hover            | Changes Colour                       | Hovered over button         | Changes Colour                        | Pass          |
| Logged Out users only                     |                                      |                             |                                       |               |
| Create Account Button                     | Navigates to the Create Account Page | Clicked Button              | Redirected to the Create account Page | Pass          |
| Create Account Button Hover               | Changes Colour                       | Hovered over button         | Changes Colour                        | Pass          |
| Already have an account link              | Navigates to the Sign In page        | Clicked Button              | Redirected to the Sign In Page        | Pass          |
| Logged In users only                      |                                      |                             |                                       |               |
| Add Holidays Button                       | Navigates to the Add Holiday Page    | Clicked Button              | Redirected to the Add Holiday Page    | Pass          |
| Add Holidays Button Hover                 | Changes Colour                       | Hovered over button         | Changes Colour                        | Pass          |
| Profile Click Here                        | Navigates to the Profile Page        | Clicked Button              | Redirected to the Profile Page        | Pass          |
| Profile Click Here  Hover                 | Changes Colour                       | Hovered over link           | Changes Colour                        | Pass          |


</details>

<details><summary>Holidays Page (Recommendations.html)</summary>

| **Feature**                               | **Expected Outcome**                                          | **Test Performed**                     | **Result**                                               | **Pass/Fail**  |
|-------------------------------------------|---------------------------------------------------------------|----------------------------------------|----------------------------------------------------------|----------------|
| All users                                 |                                                               |                                        |                                                          |                |
| Search Function                           | Filters results based on search                               | Typed in  a keyword and clicked search | Rendered holidays that realte to the search              | Pass           |
| Clear Button                              | Removes searched results and renders all holidays again       | Clicked on Clear                       | All holidays displayed on the page                       | Pass           |
| Search/Clear Button Hover                 | Changes Colour                                                | Hovered over button                    | Changes Colour                                           | Pass           |
| Jump to Map View Button                   | Navigates to the map at the bottom of the screen              | Clicked on Button                      | Directed to the map                                      | Pass           |
| Map View Button Hover                     | Changes Colour                                                | Hovered over button                    | Changes Colour                                           | Pass           |
| Holiday Card Image                        | Navigates to full page reveiw                                 | Clicked on card image                  | Redirected to full page reveiw                           | Pass           |
| Holiday Card Image Magnifying glass image | Navigates to full page reveiw                                 | Clicked on magnifying glass            | Redirected to full page reveiw                           | Pass           |
| Map Marker                                | Directs the user to the specific review for that pin          | Clicked on Markers                     | Directed to specific holiday page                        | Pass           |
| Logges In Users Only                      |                                                               |                                        |                                                          |                |
| Add Holidays Button                       | Navigates to the Add Holiday Page                             | Clicked Button                         | Redirected to the Add Holiday Page                       | Pass           |
| Add Holiday Button Hover                  | Changes Colour                                                | Hovered over button                    | Changes Colour                                           | Pass           |
| Admin Only                                |                                                               |                                        |                                                          |                |
| Delete Button                             | Brings up the confirmation Modal                              | Clicked on Button                      | Brings up confirmation Modal                             | Pass           |
| Modal No Button                           | Returns the user to the holidays page                         | Clicked No                             | Brought out of the modal, back to the holidays page      | Pass           |
| Modal Yes Button                          | Deletes the specific review and updated a new holidays page.  | Clicked Button                         | Returned to the holidays page, specific review deleted.  | Pass           |


</details>

<details><summary>Contact Page</summary>

| **Feature**     | **Expected Outcome**                                                                                   | **Test Performed**       | **Result**                                                                                           | **Pass/Fail** |
|-----------------|--------------------------------------------------------------------------------------------------------|--------------------------|------------------------------------------------------------------------------------------------------|---------------|
| All users       |                                                                                                        |                          |                                                                                                      |               |
| Input boxes     | Allow typing                                                                                           | Typed into boxes         | Form validates the input (green line)                                                                | Pass          |
| Input Boxes     | Notify user input is required                                                                          | left boxes blank         | Red line n the form, if I try to submit I'm notified which part of the form is missing.              | Pass          |
| Input Box Email | Tells the user an email address (@) is required                                                        | Inputed an invalid email | Notified to "Please include an @..."                                                                 | Pass          |
| Send Button     | Sends email to little.explorers@gmail.com with the info from the form. Notifies user the email was sent | Sent a test email        | little explorers gmail account reveives an [email](documentation/testing/images/test-email.PNG). The website notifes the user theyr email was sent! | Pass          |

</details>

<details><summary>Create Account Page</summary>

| **Feature**                  | **Expected Outcome**                                            | **Test Performed**                   | **Result**                                                                   | **Pass/Fail** |
|------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------|------------------------------------------------------------------------------------------|---------------------------|
| All users                                |                                                                             |                                                   |                                                                                          |                           |
| Input boxes                              | Allow typing                                                                | Typed into boxes                                  | Form validates the input (green line)                                                    | Pass                      |
| Input Boxes                              | Notify user input is required                                               | left boxes blank                                  | Red line in the form, if I try to submit I'm notified which part of the form is missing. | Pass                      |
| Input Box Email                          | Tells the user an email address (@) is required                             | Inputed an invalid email                          | Notified to "Please include an @..."                                                     | Pass                      |
| Input Box Check Password                 | Notified if the passwords don't match                                       | Typed an incorect Password                        | Cannot submit the form if passwords don't match                                          | Pass                      |
| Already registered email address         | Notified there is an account with this email and redirected to sign in page | Added an already in use email address             | Notified and redirected to the Sign In Page.                                             | Pass                      |
| Submit Button                            | Remains disabled until passwords match                                      | Typed correct and incorrect passwords             | Submit button is only clickable once passwords match                                     | Pass                      |
| Submit Button (Active)                   | Logs the User in and redirects to Profile Page                              | Clicked the Button                                | Notified I've been logged in (flash meesage) and redireced to Profile page               | Pass                      |
| Submit Button Hover                      | Changes Colour                                                              | Hovered over button                               | Changes Colour                                                                           | Pass                      |
| Admin Only                               |                                                                             |                                                   |                                                                                          |                           |
| Swipe button to create other admin users | Check function works and creates an admin user                              | Checked the box and looked at the subsequent uers | Admin account created                                                                    | Pass                      |


</details>

<details><summary>Profile Page</summary>

| **Feature**                           | ***Expected Outcome**                                 | **Test Performed**      | **Result**                                       | **Pass/Fail** |
|-------------------------------------------|----------------------------------------------------------|-----------------------------|------------------------------------------------------|-------------------|
| All users                                 |                                                          |                             |                                                      |                   |
| Add Holidays Button                       | Navigates to the Add Holiday Page                        | Clicked Button              | Redirected to the Add Holiday Page                   | Pass              |
| Add Holiday Button Hover                  | Changes Colour                                           | Hovered over button         | Changes Colour                                       | Pass              |
| Holiday Card Image                        | Navigates to full page reveiw                            | Clicked on card image       | Redirected to full page reveiw                       | Pass              |
| Holiday Card Image Magnifying glass image | Navigates to full page reveiw                            | Clicked on magnifying glass | Redirected to full page reveiw                       | Pass              |
| Edit/Delete Buttons Hover                 | Change Colour                                            | Hovered over buttons        | Change Colour                                        | Pass              |
| Edit Button                               | Redirects to the Edit Recommendation (Holiday) Page.     | Clicked Button              | Redirected to the Edit Recommendation (Holiday) Page | Pass              |
| Delete Button                             | Brings up the confirmation Modal                         | Clicked on Button           | Brings up confirmation Modal                         | Pass              |
| Modal No Button                           | Returns the user to the holidays page                    | Clicked No                  | Brought out of the modal, back to the holidays page  | Pass              |
| Modal Yes Button                          | Deletes the specific review and loads a new profile page | Clicked Button              | Returned to the profile, specific review deleted.    | Pass              |
| Admin Only Users                          |                                                          |                             |                                                      |                   |
| Navigate to admin features button         | Navigates to the bottom of the page, admin features      | Clicked Button              | Moved down the page to the admin content             | Pass              |
| Navigate to admin Button Hover            | Changes Colour                                           | Hovered over button         | Changes Colour                                       | Pass              |
| Users/Holiday Tuypes/Holiday Buttons      | Change Colour                                            | Hovered over buttons        | Change Colour                                        | Pass              |
| Users Button                              | Navigates to the Users Management Page                   | Clicked Button              | Redirected to the Users page                         | Pass              |
| Holiday Types Button                      | Navigates to the Holiday Types Page                      | Clicked Button              | Redirected to the Holiday Types page                 | Pass              |
| Holidays Button                           | Navigates to the Holidays Page                           | Clicked Button              | Redirected to the Holidays page                      | Pass              |


</details>

<details><summary>Add Holiday Page</summary>

| **Feature**        | **Expected Outcome**                                           | **Test Performed**                        | ***Result**                                                                            | **Pass/Fail** |
|------------------------|-----------------------------------------------------------------------|-----------------------------------------------|-------------------------------------------------------------------------------------------|-------------------|
| All users              |                                                                       |                                               |                                                                                           |                   |
| Input Boxes            | Notify user input is required                                         | left boxes each box blank and tried to submit | Red line in the form, if I try to submit I'm notified which part of the form is missing.  | Pass              |
| Address Input          | Allows a user to type an address (and get drop down suggestions).     | Started Typing an address                     | Addresses are suggested and clickable                                                     | Pass              |
| Address Input from Map | Address is auto generated from where the map pin is positioned.       | Moved map pin                                 | Address is auto-poulated                                                                  | Pass              |
| Map Marker             | Moves when the address is inputed                                     | Typed in an address                           | Map Marker moves to correct position                                                      | Pass              |
| Character Count        | Counts down how many characters are remaining in the review text area | Typed in the review box                       | Remaining characters box updated with each character typed.                               | Pass              |
| Image file             | Only allows Images to be uploaded                                     | Added a PDF to the form                       | Notifed that I must select a file with the format jpeg, jpg or png                        | Pass              |
| Image View Button      | Allows the user to see what image they have uploaded                  | Added an image file and clicked View          | image is displayed on the page                                                            | Pass              |
| Sumbit Button          | Sends the form/data and returns user to their profile page            | Submitted the form using the button           | Returned to the Profile page with the added holiday displayed                             | Pass              |
| Submit Button Hover    | Changes Colour                                                        | Hovered over button                           | Changes Colour                                                                            | Pass              |


</details>

<details><summary>Sign Out</summary>

</details>

Admin Only Features

<details><summary>Holiday Types Page</summary>
| **Feature**                | **Expected Outcome**                                     | **Test Performed**   | **Result**                                          | **Pass/Fail** |
|----------------------------|----------------------------------------------------------|----------------------|-----------------------------------------------------|---------------|
| Add Holiday Type Button    | Navigates to the Add Holiday Type Page                   | Clicked Button       | Redirected to the Add Holiday Type Page             | Pass          |
| Add Holiday Button Hover   | Changes Colour                                           | Hovered over button  | Changes Colour                                      | Pass          |
| Edit/Delete Buttons Hover  | Change Colour                                            | Hovered over buttons | Change Colour                                       | Pass          |
| Edit Button                | Redirects to the Edit Holiday Type Page.                 | Clicked Button       | Redirected to the Edit Holiday Type Page            | Pass          |
| Delete Button              | Brings up the confirmation Modal                         | Clicked on Button    | Brings up confirmation Modal                        | Pass          |
| Modal No Button            | Returns the user to the holidays page                    | Clicked No           | Brought out of the modal, back to the holidays page | Pass          |
| Modal Yes Button           | Deletes the specific review and loads a new profile page | Clicked Button       | Returned to the profile, specific review deleted.   | Pass          |

</details>

<details><summary>Add Holiday Types Page</summary>

| **Feature**         | **Expected Outcome**                                           | **Test Performed**                                      | **Result**                                                                                | **Pass/Fail** |
|---------------------|----------------------------------------------------------------|---------------------------------------------------------|-------------------------------------------------------------------------------------------|---------------|
| Input Boxes         | Notify user input is required                                  | left boxes each box blank and tried to submit           | Red line in the form, if I try to submit I'm notified which part of the form is missing.  | Pass          |
| Select Icon Button  | Allows the user to pick an icon for the holiday type           | Clicked on different "Select"'s to pick different icons | Icon image updated in the input box                                                       | Pass          |
| Submit Button       | Sends the form/data and returns user to the holiday types page | Submitted the form using the button                     | Returned to the Holiday Types Page with the Holiday Type added                            | Pass          |
| Submit Button Hover | Changes Colour                                                 | Hovered over button                                     | Changes Colour                                                                            | Pass          |

</details>

<details><summary>Users</summary>

| **Feature**                  | **Expected Outcome**                                                            | **Test Performed**  | **Result**                                         | **Pass/Fail** |
|------------------------------|---------------------------------------------------------------------------------|---------------------|----------------------------------------------------|---------------|
| Search Input + Search Button | Returns Users from username/email address info                                  | Typed in a user     | Shown specific user                                | Pass          |
| Clear Button                 | Removes searched results and renders all holidays again                         | Clicked on Clear    | All holidays displayed on the page                 | Pass          |
| Search/Clear Button Hover    | Changes Colour                                                                  | Hovered over button | Changes Colour                                     | Pass          |
| Delete Button Hover          | Change Colour                                                                   | Hovered over button | Changes Colour                                     | Pass          |
| Delete Button                | Brings up the confirmation Modal                                                | Clicked on Button   | Brings up confirmation Modal                       | Pass          |
| Modal No Button              | Returns the user to the users page                                              | Clicked No          | Brought out of the modal, back to the users page   | Pass          |
| Modal Yes Button             | Deletes the specific User (and associated holidays) and loads updated user page | Clicked Button      | Returned to the user page, specific user deleted.  | Pass          |


</details>


LEFT TO DO:

<details><summary>Edit Holiday</summary>

</details>

<details><summary>Edit Holiday Type</summary>

</details>

<details><summary>Sign Out</summary>

</details>



## Testing User Stories

** My User story testing

## Real User Testing

Little Explorers was reviewed by friends and family. They were encouraged to comment on their user experience and feedback on any bugs they found. In each testing environment, users were asked to pay particular attention to the buttons and the overall look of the page.

Comments from User 1 (iphone 13 ):

1:

- Comment: "It is difficult to know how much of the review space you have left when you're typing, a countdown on character's left would be helpful"

- Action Taken: A character countdown paragraph was added to notify the users of their remaining entitlemnt. this was imnpletments using javascript. 

2:

- Comment: "When tyring to select a holiday type when adding a recommended holiday, the drop down menu doesn't always register what they pressed."  

- Action Taken: After researching this issue, I found that it is a common and well-documented problem with Materialize select boxes. [This post](https://github.com/Dogfalo/materialize/issues/6464) identified a patch that I could implement to resolve the issue. Further testing by the user confirmed that this solution was successful.

3:

- Comment: "I couldn't find an option that I wanted as my holiday didn't fit under any of your catagories"

- Action Taken: I have added an "Other" catagory to pick these up. an admin could group them accordignly as the site grew it's database. 

4:

- Comment: "It would be better if the image on the holidays page, also took you to the main reveiw page, rather than just the magnifying glass."

- Action Taken: I have added code so that the image is also a clickable link.  

5:

- Comment: "Is it possible to add a part which allows you to know the ages of the children, so I could filter by holidays suitable for a 3yr old for example"

- Action Taken: This comment has picked up a feature that would be very valuble to this website. However, to implement it would reqire signficant restructuring of the database, the displayed information and the search functionality. Therefore at this time, I have not made changes to respond to this comment but they should be addressed for future roll outs.  

6:

- Comment: "It could be nice to let the user add a link to the air b and b/place they stayed or to link to places they visited"

- Action Taken: As above.  