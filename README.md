[![Build Status](https://travis-ci.org/AlexiaDelorme/project-spacex.svg?branch=master)](https://travis-ci.org/AlexiaDelorme/project-spacex)

# [SpaceX]()

## Table of Contents
1. [UX](#ux)
    - [User Stories](#user-stories)
    - [Design](#design)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Current Features](#current-features)
    - [Future Features](#future-features)

3. [Database](#database)
    - [Database choice](#db-choice)
    - [Database structure](#db-structure)

4. [Technologies Used](#tech)
    - [Languages](#languages)
    - [Libraries](#libraries)
    - [Tools](#tools)

5. [Testing](#testing)

6. [Deployment](#deployment)
    - [Heroku Deployment](#depl-heroku)
    - [Local Deployment (GitPod)](#depl-gitpod)

7. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#ack)

<a name="ux"/>

# UX

**Project definition**
- “SpaceX" is the first ever travel agency that organizes trips to space with multiple destinations in close collaboration with aerospace entities and governments. 
- The purpose of this web app is to provide customers who would like to travel to space with an online platform where they can book for their very first trip to space. 
- Users can browse for all the trips that are offered by the space travel agency. 
- Different types of trips are offered according to the type of client. 

**Project stakeholders**
- Individuals – the agency offers recreational space travels for individuals.
- Businesses & scientists – the agency offers space travels for businesses and scientists for research purposes.

<a name="user-stories"/>

## User Stories

As a general user, I expect:
1. To have convenient access of all the trips that the travel agency offers.
2. The website to have a neat and elegant design with an optimal architecture and layout.
3. The website to be intuitive and easy to navigate so that I can find what I need in the most effective manner.
4. To easily find information i.e. identify key information for a specific trips and if needed, be able to get access to more details.
5. To easily find information about the travel company and see their entire range of offers. I also want to have their contact details and be able to get in touch with them through a contact form.  
6. To be able to research trips by destination, departure site and date.
7. To read testimonies from previous customers so that I have a clear vision of the experience offered. 
8. To be advised of the remaining slots if the trip is almost sold out and register to a waiting list if it is already sold out. 
9. To be able to book a trip and then be able to register/log in to an account with minimal steps to confirm my order.
10. The website to display my order details for each steps of the checkout and receive an email once my booking has been completed. 
11. The website to be fully responsive on any devices: mobile, tablet, desktop. 
12. The website to be fully interactive so that I get clear feedback on any action I undertake (complete a form, process a payment, log in, log out etc…).
13. As a business or scientist, I want to easily find information on the application process and gets a pricing estimate for my request. 
14. As a user, I want to be able to access (and update) my personal information, upcoming and post bookings.

<a name="design"/>

## Design

### Theme

I wanted to create a website that would transport the user to space. I wanted to keep it classy and professional as well. I have tried to put some efforts on selecting visually impacting pictures. 

I have used a free bootstrap theme called [Grayscale](https://startbootstrap.com/themes/grayscale/). I found it absolutely wonderful and I tried my best to stick to the theme while building my website.

### Colors

The three main colors were used throughout this project.

1. White - ` #fff`
    - Background
    - Navbar
2. Black - `#161616`
    - background
3. Green - `#64a19d`
    - Buttons
    - Links
    - Some icones

### Typography

- The primary font family is [Nunito](https://fonts.google.com/specimen/Nunito) from Google Fonts.
- The second font family - used mainly for headers - is [Varela Round](https://fonts.google.com/specimen/Varela+Round?selection.family=Varela+Round&sidebar.open) also from Google Fonts.

<a name="wireframes"/>

## Wireframes

I have used Balsamiq to create my wireframes. I first brainstormed on the structure and then created the site map. There are some differences with the final project as these wireframes were created during the preparation phase. 

- [Site map](https://i.ibb.co/3kRsBpC/Site-map.png)
- [Home](https://i.ibb.co/wJV0cz1/Home.png)
- [About](https://i.ibb.co/nkDJLLv/About.png)
- [Contact](https://i.ibb.co/r0NdrSH/Contact.png)
- [Faqs](https://i.ibb.co/8XQKgk7/FAQs.png)
- [Trips](https://i.ibb.co/0FN5kv8/Trips.png)
- [Listing](https://i.ibb.co/jbJDKtx/Listings.png)
- [Cart](https://i.ibb.co/wCrWvJQ/Checkout-Booking-confirmation.png)
- [Checkout 1](https://i.ibb.co/hsKMCm0/Checkout-Info.png)
- [Checkout 2](https://i.ibb.co/55gyb6m/Checkout-Payment.png)
- [Checkout 3](https://i.ibb.co/ZKWpnMb/Checkout-Confirmation.png)
- [Profile](https://i.ibb.co/DkWgrjC/Account.png)

<a name="features"/>

# Features

<a name="current-features"/>

## Current Features

###### Features on every page
- xx

###### Feature 1

<a name="future-features"/>

## Future Features

<a name="database"/>

# Database

<a name="db-choice"/>

## Database choice

### Trip model

        | Name | Key in db | Validation | Field Type |
        | ------------- | ------------- | ------------- | ------------- |
        | Departure site | departure_site | on_delete=models.PROTECT | ForeignKey(Departure Site) |
        | Departure date | departure_date |  | DateField() |

<a name="db-structure"/>

## Database structure

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

##### [Django 3](https://www.djangoproject.com)
- I used Django 3 as my Python framework to build this website. 

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

##### [Balsamiq](https://balsamiq.com/) 
- I used Balsamiq to design my wireframes during the planning phase of this project.

##### [Gitpod](https://gitpod.io/)
- During this project, I migrated to Gitpod as my credentials for AWS Cloud 9 expired.
- I therefore completed this project using Gitpod IDE. 

##### [Postgres]()
- 

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
- 

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
- [Progress tracker](https://stackoverflow.com/questions/5213753/build-step-progress-bar-css-and-jquery)
- [Login success view](https://stackoverflow.com/questions/16824004/django-conditional-login-redirect/16824337#16824337)

<a name="ack"/>

### Acknowledgements
- My Code Institute mentor, Nishant Kumar, for his patience and great support throughout this project.
- Kevin from the Code Institute Tutor Team for helping me set up a "login success" view to enable users to be redirected back to the checkout page if they had to register to an account.