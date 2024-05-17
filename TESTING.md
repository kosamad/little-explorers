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

- Action Taken: I have tried to replicate this error but using my pixel 4, the issue doesn't arise and I don't have an apple device to complete thourough testing. This would need to be addressed before a wide-spread roll out. 

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