[![Build Status](https://travis-ci.org/AlexiaDelorme/project-spacex.svg?branch=master)](https://travis-ci.org/AlexiaDelorme/project-spacex)

# [SpaceX]()

Project currently under early stage of development. 

## Table of Contents
1. [UX](#ux)
    - [User Stories](#user-stories)
    - [Design](#design)
    - [Wireframes](#wireframes)
    - [Flowchart](#flowchart)
    - [Database structure](#db)

2. [Features](#features)
    - [Current Features](#current-features)
    - [Future Features](#future-features)

3. [Technologies Used](#tech)
    - [Languages](#languages)
    - [Libraries](#libraries)
    - [Tools](#tools)

4. [Testing](#testing)

5. [Deployment](#deployment)
    - [Heroku Deployment](#depl-heroku)
    - [Local Deployment (GitPod)](#depl-gitpod)

6. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#ack)

<a name="ux"/>

# UX

**Project definition**
- “SpaceX" is the first ever travel agency that organizes trips in space with multiple destinations in close collaboration with aerospace entities and governments. 
- The purpose of this web app is to provide customers who would like to travel to space with an online platform where they can book for their very first trip to space. 
- Users can browse for all the trips that are offered by the space travel agency. 
- Different types of trips are offered according to the clients type. 

**Project stakeholders**
- Individuals – the agency offers recreational space travels for individuals.
- Businesses & scientists – the agency offers space travels for businesses and scientists for research purposes.

<a name="user-stories"/>

## User Stories

As a general user, I expect:
- To have convenient access of all the trips that the travel agency offers.
- The website to have a neat and elegant design with an optimal architecture and layout.
- The website to be intuitive and easy to navigate so that I can find what I need in the most effective manner.
- To easily find information i.e. identify key information for a specific trips and if needed, be able to get access to more details.
- To easily find information about the travel company and see their entire range of offers. I also want to have their contact details and be able to get in touch with them through a contact form.  
- To be able to research trips based on specific filters such as the client’s type, price, duration, pictures… 
- To read testimonies from previous customers so that I have a clear vision of the experience offered. 
- To be advised of the remaining slots if the trip is almost sold out and register to a waiting list if it is already sold out. 
- To be able to book a trip and then be able to register/log in to an account with minimal steps to confirm my order.
- The website to display my order details for each steps of the checkout (booking till payment) and receive an email once my booking has been completed. 
- The website to be fully responsive on any devices: mobile, tablet, desktop. 
- The website to be fully interactive so that I get clear feedback on any action I undertake (complete a form, process a payment, log in, log out etc…).
- As a business or scientist, I want to easily find information on the application process and gets a pricing estimate for my request. 
- As a logged in user, I want to be able to access my information details (personal information and past bookings), update them and delete my account permanently if necessary. 

<a name="design"/>

## Design

### Theme

### Colors

### Typography

<a name="wireframes"/>

## Wireframes

I have used Balsamiq to create my wireframes. I first brainstormed on the structure and then created the site map. There are of course some differences with the final project as these wireframes were created during the preparation phase. 

You can find all my wireframes below:
(To be updated)
- Home page
- ...

<a name="flowchart"/>

## Flowchart

<a name="db"/>

## Database structure

<a name="features"/>

# Features

<a name="current-features"/>

## Current Features

###### Features on every page
- xx

###### Feature 1

<a name="future-features"/>

## Future Features

<a name="tech"/>

# Technologies Used

<a name="languages"/>

## Languages

##### [HTML5](https://www.w3.org/TR/html/)
- I used HTML to create the static content of my website.
- The following [code validator](https://validator.w3.org/) was used to test my HTML code.

##### [CSS3](https://www.w3.org/Style/CSS/)
- I used CSS to style my website and personalize it.  
- The following [code validator](https://jigsaw.w3.org/css-validator/) was used to test my CSS code.

##### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- I used core JS in coordination with Sweet Alert library.
- [JSHint](https://jshint.com/) was used to check my JS code quality.

##### [Python 3](https://www.python.org/downloads/release/python-374/)
- I used Python 3 as the back-end programming language for my application.

<a name="libraries"/>

## Libraries

##### [Django](https://www.djangoproject.com)
- I used Django as my Python framework to build this website. 

##### [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)
- ?

##### [Bootstrap](https://getbootstrap.com/)
- I used Bootstrap as the main framework for HTML.

##### [jQuery](https://jquery.com/) 
- I used jQuery to simplify the DOM manipulation.

##### [Font Awesome](https://origin.fontawesome.com/)
- I used Font Awesome to display social media icons for my footer.

##### [Google Fonts](https://fonts.google.com/)
- I used one of Google fonts for my website.

<a name="tools"/>

## Tools

##### [draw.io](https://www.draw.io#)
- I used this diagram tool to structure my data flow during the planning phase of this project.

##### [Balsamiq](https://balsamiq.com/) 
- I used Balsamiq to design my wireframes during the planning phase of this project.

##### [Gitpod](https://gitpod.io/)
- During this project, I migrated to Gitpod as my credentials for AWS Cloud 9 expired.
- I therefore completed this project using Gitpod IDE. 

##### [Postgres or MySQL]()
- ?

##### [Git & GitHub](https://github.com/)
- I used Git for version control. 
- I used GitHub to store my code in a remote repository.

##### [Heroku](https://dashboard.heroku.com)
- I used Heroku to deploy and host my application.

##### [TinyPNG](https://tinypng.com)
- I used TinyPNG to optimize the size of my images.

<a name="testing"/>

# Testing 

All the documentation regarding the testing of this project can be found in this [TESTING.md](testing/TESTING.md) file.

<a name="deployment"/>

# Deployment

<a name="depl-heroku"/>

## Heroku

My application was deployed through [heroku](https://dashboard.heroku.com) using the master branch of my github repository for this project. The following steps were implemented to deploy this project:

1. Install gunicorn package to run the application on Heroku.
    - `sudo pip3 install gunicorn`
2. Install pycopg2 to connect to PostgreSQL
    - `sudo pip3 install psycopg2`
3. Create a **requirements.txt** file
    - `sudo pip3 freeze --local > requirements.txt`
4. Install PostgreSQL add-on
    - `heroku addons:create heroku-postgresql:hobby-dev`
4. Create a **Procfile**
    - `to be updated`
5. Create a new Heroku application
    - Sign up to a new account if you do not already have one.
    - Create a new application by clicking on `new` then `create new app`.
    - Set the name of your application and select your region and click on `create app` to finalize the creation of your app. 
6. Set the following config variables as environment variables:
    - **SECRET_KEY**: `<SECRET_KEY>`

To be updated

5. In the `Deploy` tab, choose `Connect Github` as **Deployment Method** and *Enable Automatic Deployment* from the Github master branch so that any new commit will be automatically deployed through your heroku app. 

<a name="depl-gitpod"/>

## Local Deployment (GitPod)

To deploy this project locally using gitpod you will have to create a gitpod account and use a web browser with a stable internet connection as gitpod is an online IDE. I suggest you use Chrome as web browser so that you can use gitpod chrome extension to speed up the deployment process. 

1. Create a Gitpod account (if not already)
    - Go to [GitPod](https://www.gitpod.io)
    - Click on `Go to App` and click on the green `Authorize gitpod.io`
    - Agree to the terms and then create your free account
2. Add gitpod browser extension for Chrome:
    - Go to [GitPod Chrome Browser Extension](https://chrome.google.com/webstore/detail/gitpod-online-ide/dodmmooeoklaejobgleioelladacbeki)
    - Search for "gitpod" in chrome web store search bar
    - Click on `Add to Chrome` then click on `Add to extension`
3. Clone this project repository from github
    - Go to my [repository]() for this project.
    - If you successfully installed the gitpod browser extension you should view a green `Gitpod` button in the top right corner of the repository (next to `Clone or download` button). Click the `Gitpod` button. 
    - This will allow to open this repository directly in gitpod for editing.
4. Set environment variables for the project
To be updated

5. db ? 
To be updated

6. Download all the dependencies necessary to run this project and listed in the **requirements.txt** file. 
    - Run the following command `pip3 install -r requirements.txt`

7. Create a local development server:
    - In the workspace run the following command `Python3 manage.py runserver`.
    - You should now have a gitpod link to the deployed app. 

<a name="credits"/>

# Credits

<a name="content"/>

### Content
- xx

<a name="media"/>

### Media

- The logo I used for this website was created thanks to [Hatchful](https://hatchful.shopify.com).
- All the images used for this project were found on [Pexels](https://www.pexels.com).
- I also used [Font Awesome](https://fontawesome.com/v4.7.0/icons/) on some icons when I could not find the proper icon in the Materialize icon library.
- Gif used in 404 and access_denied pages: [Dribble](https://dribbble.com/search/shots/popular/animation?q=dessert)
- Colours of footer incons when hovered: [encycolorpedia.fr](https://encycolorpedia.fr/00acee)
- Demo picture of my app used in this README file: [Am I Responsive](http://ami.responsivedesign.is/#)

<a name="code"/>

### Code
- [Datepicker](https://jsbin.com/culagonula/edit?html,js,output)
- [Timeline](https://bootsnipp.com/tags/timeline/4)
- [Collapsable](http://jsfiddle.net/hungerpain/eK8X5/7/)

<a name="ack"/>

### Acknowledgements
- My Code Institute mentor, Nishant Kumar, for his patience and great support throughout this project! 
- xx