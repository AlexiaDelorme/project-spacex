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
- Gitpod extension for Python and Pylint-django was used to check the code quality for Python files. TO BE UPDATED

<a name="python"/>

### Python

<a name="js"/>

### JS

<a name="travis"/>

### Travis

<a name="manual-tests"/>

## Manual tests

<a name="user-stories"/>

### User stories

This project has been tested multiple times against each user stories listed in the UX section of the [README.md](../README.md) file. 

1. User story 1 testing

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