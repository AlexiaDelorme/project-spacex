# Testing File

Back to [README.md](../README.md)

## Table of Contents

1. [Automated Tests](#automated-tests)
    - [Code quality](#code-quality)
    - [Python](#python)
    - [JS](#js)
    - [Travis](#travis)

2. [Manual tests](#manual-tests)
    - [User stories](#user-stories)
    - [Features](#features)
    - [Compatibility & Responsiveness](#compatibility)

3. [Known issues](#known-issues)
    - [Solved](#solved)
    - [Unsolved](#unsolved)

<a name="automated-tests"/>

## Automated Tests

<a name="code-quality"/>

### Code quality

- [W3C Markup Validation](https://validator.w3.org/) was used to check the code quality for HTML files.
- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) was used to check the code quality for CSS files.
- [JSHint](https://jshint.com/) was used to check the code quality for JS files.
    - The following undefined variables were reported but they are all related to the use of APIs: emailjs, google, stripe, csrftoken, swal.
    - There are two syntax warnings related to the use of syntax only available in ES6.
- I used Visual Studio Code extension for Python available in Gitpod to ensure the code quality of my Python files. 

<a name="python"/>

### Python

I have tested my Python files using Django test framework that is built on unittest. For each app, I have created a tests folder in which I have tested - if relevant - the following files:
- urls.py
- views.py
- models.py
- forms.py

#### How to run Python tests

1. Run the following command in the terminal: `python3 manage.py test`
2. If you want to only run test for a specific app, then you can run the following command: `python3 manage.py test <app_name>`
3. In the terminal, you should view how many tests have run and the time it took to run those tests. 

#### Coverage

1. Run the following command in the terminal: `coverage run --source='.' manage.py test`
2. If you want to only run test coverage for a specific app, then you can run the following command: `coverage run --source='<app_name>' manage.py test <app_name>`
3. Then, to view the coverage report in the terminal, run the following command: `coverage report`
4. If you would like to have details about code coverage for a specific file you can:
    1. first run: `coverage html`
        It should create a folder called 'htmlcov'
    2. then run: `python3 -m http.server`
        You should be able to open the folder 'htmlcov' and then check in details for each python files the coverage.

I have managed to achieve a coverage of 95% on my project. I have 'N' (TO BE UPDATED) tests that are all passing. 

#### Missing automated tests

<a name="js"/>

### JS

For this project, JavaScript was mainly used for DOM manipulation and ajax calls. I have therefore decided to test all these functionalities manually in the [section](#manual-tests) that comes next.

<a name="travis"/>

### Travis

During the entire development of this project, I used [Travis](https://travis-ci.org/) to ensure continuous integration of the deployed site. 

<a name="manual-tests"/>

## Manual tests

<a name="user-stories"/>

### User stories

This project has been tested multiple times against each user stories listed in the UX section of the [README.md](../README.md) file.

**As a user, I expect:**
1. **To have convenient access of all the trips that the travel agency offers.**
    - The user can easily identify the 'Trips' menu in the navigation bar.
    - The user has the option to look for all the trips available by clicking on 'Search all' in the dropdown menu.
    - If the user only wants to look for the type of destination available, (s)he can click on 'Destination' in the dropdown menu. 
2. **The website to have a neat and elegant design with an optimal architecture and layout.**
    - The website is consistent with regards to the design and layout. 
    - All the images are visually impacting and related with astrophysics and space.
3. **The website to be intuitive and easy to navigate so that I can find what I need in the most effective manner.**
    - The website has a simple architecture and is quite intuitive to navigate. 
    - All important pages can be accessed through a fixed navbar bar that is therefore always available for the user.
    - Some useful links are also available on the footer (trips, scientists and faq).
4. **To easily find information i.e. identify key information for a specific trips and if needed, be able to get access to more details.**
    - The user can have access to trips presented by destination. Key information is listed in an organized manner: trip destination, trip duration, trip distance...
    - The user can access more details about the destination by clicking on the 'trip details' button. The user will be able to view more pictures of the destination, with key information, and a detailed trip description. 
5. **To easily find information about the travel company and see their entire range of offers. I also want to have their contact details and be able to get in touch with them through a contact form.**
    - The user can easily access information about the travel company by clicking on the 'About' item in the navbar. On this page, the user will have access to a small presentation of the company along with their history and all the services they provide.
    - The user can get in touch with the company through a contact form available in the 'Contact' page. 
6. **To be able to research trips by destination, departure site and date.**
    - The user can research trip by destination and then on the trip details, (s)he will have the option to submit a form to look for all the available trips for this specific destination.
    - The user can also research trips in the 'Search all' section. At the top of the results page, there is a search form where the user can look for trips with the following criteria: destination, departure site and departure date. 
7. **To read testimonies from previous passengers and have access to FAQs.**
    - Testimonies from previous passengers are directly available on the home page.
    - A link to the FAQs is available in the 'trips' dropdown menu in the navbar and in the footer as well. 
8. **To be able to book a trip and then register/log in to an account with minimal steps to confirm my order.**
    - After looking for a trip, the user can easily add the trip to his/her cart. The user will be then redirected to the cart page to view the content of his/her cart. Then, the user will be able to proceed to the checkout by clicking the button at the end of the cart page.
    - If the user is already logged in, (s)he will be able to start the checkout process.
    - Otherwise, the user will be able to log in / register to an account and then be redirected back to the checkout process. 
9. **The website to display my order details for each steps of the checkout and receive an email once my booking has been completed.**
    - For each step of the checkout process, a recap of the user's booking with key information related to the trip(s) is displayed.
    - The different steps of the checkout are very clear and indicated at the top of each page thanks to a progress bar. 
    - SEND EMAIL AFTER BOOKING IS COMPLETED IS TO BE DONE. 
10. **The website to be fully responsive on any devices: mobile, tablet, desktop.**
    - This project has been created to be fully responsive on all devices' size. For each page, the wireframes are available in three sizes.
    - Throught the developement of this project, it has been extensively tested on mobile, tablet and desktop as well as on other devices screen size available in Chrome Developer Tools. 
11. **The website to be fully interactive so that I get clear feedback on any action I undertake (complete a form, process a payment, log in, log out etc…).**
    - Flash messages were used to provide feedback to the user anytime an action has been triggered by the user leading to be redirected to a different view. Flash messages were used to provide feedback to the user if an action has indeed taken place when the user should be redirected to a different view than the one (s)he initiated the action.
    - SweetAlert was used to provide feedback thanks to an alert box when the user has requested an action but this action requires a confirmation or just to provide feedback that this action is not permitted. For instance, when the user is adding a trip to his cart, then it will be asked to confirm if (s)he would like to keep shopping or go to the cart. Also JS was prioritized to provide feedback when the action the user has initiated does not imply that the user will be redirected to a different view.
12. As a business or scientist, I want to easily find information on the application process and request information to the company. 
    - Scientists and businesses have a dedicated page available from the navbar by clicking on 'Scientists'. 
    - On this dedicated page, they can find information on the selection process for a scientific experiment, examples of past experiments etc... A link to the contact page is also available on this page.
13. As a user, I want to be able to access (and update) my personal information, upcoming and post bookings.
    - The user has access to their personal information on their 'Profile' page. The user can update their contact details, passenger details as well as their password.
    - The user can access their upcoming or past bookings by clicking on the 'Bookings' link in the 'Account' dropdown menu in the navbar. 

<a name="features"/>

### Features

###### Features on every pages

1. Navbar

**Test scenario:**
- [x] Check that each following menu items display correctly when the user is not logged in (and following this order): The Pâtisserie Logo, Home, Explore, Recipes, About, Sign Up and Log In. 
- [x] Hover over each menu items and confirm that the background colour changes from white to grey. 
- [x] Click on `The Pâtisserie` logo, it should take the user back to the home page.
- [x] Click on `Home`, it should take the user back to the home page.
- [x] Click on `Explore`, it should take the user to the explore recipes page.
- [x] Click on `Recipes`, it should take the user to the recipes by categories page.
- [x] Click on `About`, it should take the user to the about page.
- [x] Click on `Sign Up`, it should take the user to the sign up page.
- [x] Click on `Log In`, it should take the user to the log in page.

**Test result:** Successful :white_check_mark:

*Specific test undertaken for mobile and tablet devices:*

**Test scenario:**
- [x] Open the website on a mobile or a tablet and confirm that the navbar is collapsed into a hamburger button (the logo should still be visible).
- [x] Click on the hamburger button and confirm that the menu items are correctly displayed and that each link refers to the corresponding page. 
- [x] When logged in/out, confirm that you have the expected view.

**Test result:** Successful :white_check_mark:

2. Footer 

**Test scenario:**
- [x] Confirm that the icons in the footer display correctly in the following order: Facebook, Instagram, Youtube, Pinterest and Twitter.
- [x] Hover over each icons and confirm that their colours change to the social media "referenced" colour. Example: Facebook icon should turn dark blue, Youtube icon should turn red...
- [x] Click on each social media icon, it should take the user to the corresponding social media page, opening in a new tab. It takes the user to the home page of each social media as this is a mock project - no account was created.  

**Test result:** Successful :white_check_mark:

###### Feature 1 - Home page

**Hypothesis:** The user should be logged out to perform this test.

**Test scenario:**
- [x] The title and the picture of the welcome page loaded successfully. 
- Our recipes section   
    - [x] When scrolling down, the user should first see a section teaser for recipes. 
    - [x] Confirm that the three pictures loaded successfully. 
    - [x] When the user hovers over `EXPLORE RECIPES`, the font colour should turn pink and the border below should expand. 
    - [x] Click on `EXPLORE RECIPES`, it should take the user to the explore recipes page. 
- Online cookbook section
    - [x] When scrolling down, the user should then see a section teaser for the online cookbook. 
    - [x] Confirm that the picture loaded successfully. 
    - [x] When the user hovers over `JOIN US`, the font colour should turn pink and the border below should expand. 
    - [x] Click on `JOIN US`, it should take the user to the sign up page. 
- About us section
    - [x] When scrolling down, the user should finally see a section teaser to present the website.  
    - [x] Confirm that the picture loaded successfully. 
    - [x] When the user hovers over `LEARN MORE`, the font colour should turn pink and the border below should expand. 
    - [x] Click on `LEARN MORE`, it should take the user to the sign up page. 

**Test result:** Successful :white_check_mark:

<a name="compatibility"/>

### Compatibility & Responsiveness

###### Compatibility

A manual cross-browser testing was performed for each features for the following browsers:
- Safari
- Google Chrome 
- Mozilla Firefox
- Opera

###### Responsiveness

The responsiveness of the webiste was tested thanks to Google Chrome developer tool, the following devices size were tested for all features and all elements were displayed without issues:
- Galaxy S5 
- Pixel 2 / Pixel 2 XL 
- iPhone 5/SE
- iPhone 6/7/8 and Plus
- iPhone X 
- iPad / iPad Pro 

The automated tool [BrowserStack](https://www.browserstack.com) was also used to review responsiveness on a wide range of devices. 

<a name="known-issues"/>

## Known Issues

While testing this project some bugs were discovered and they have been documented in the section down below. 

<a name="solved"/>

### Solved Issues

1. Solved issue 1

<a name="unsolved"/>

### Unsolved Issues

1. Unsolved issue 1