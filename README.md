# MyCar
![Main Page](https://res.cloudinary.com/shahid129/image/upload/v1665405565/static/images/main-min_dly8td.png)

[View Live Project Here](https://shahid-my-car.herokuapp.com/)

## TABLE OF CONTENTS
- [Introduction](#introduction)
- [User Experience/User Interface](#user-experience-or-user-interface)
- [Design](#design)
- [Features](#features)
- [Testing](#testing)
- [Technology](#technology)
- [Deployment](#deployment) 
- [Credits](#credits)
- [Acknowledgement](#acknowledgement)

## Introduction
MyCar is a website for selling and buying cars. Anyone can view cars listed on the website. To sell a car the user has to create an account and add a listing. Options for buying a car are not available at the minute. But this would be a future feature where users can buy as well. Once an id is created for selling a car, the user will get a verification email to confirm their registration. A profile is also created upon registration which they can update if they wish to. A seller is given the flexibility to create a listing, and edit or delete it. There is also a search option where anyone can search for a car.

## User Experience or User Interface

### Agile
The plan for this project was carried out using the Agile Methodology in Github. User Stories were created using the issues on the git hub. Each user story explicitly explains the purpose of the issues. Each user story is segmented into acceptance criteria and tasks. It was prioritised using GitHub labels with different colors. The labels are should have, could have and must have. Once the issues are created they are moved to the User Stories kanban board. The Kanban board has three main columns, To Do, In Progress and Done. Once you start working with the user story, you move it to the To Do column and when finished move it to the Done column. Following this pattern of work gives you a full-on idea about the progress of the project.

### User Stories

There are 18 user stories.
- Site Pagination
    - As a Site User I can View a paginated list of posts so that I can easily select a post to vew (must have / complete) [[#1](https://github.com/shahid129/mycar/issues/1)]

- Login and Logout 

    - As a User I can I can login and logout so that I can access my content (must have / complete) [[#2](https://github.com/shahid129/mycar/issues/2)]

 -  Comments 
    
    - As a User I can Comment on a content so that *I can involve in the conversation (must have / complete) [[#3](https://github.com/shahid129/mycar/issues/3)]

-  Register Account 
    - As a User I can Register an account so that I can post my add and comments (must have / complete) [[#4](https://github.com/shahid129/mycar/issues/4)]

-  Approve comments
    - As an Admin I can access the user comments so that I can remove the inappropriate contents from the page (must have / complete) [[#5](https://github.com/shahid129/mycar/issues/5)]
- CRUD Functionalities
    - As a User I can Create, read, update and delete items so that I have control on my post and contents (must have / complete) [[#6](https://github.com/shahid129/mycar/issues/6)]
- Like a post
    - As a User I can Like a post and see the number of likes so that I know which posts are popular (must have / complete) [[#7](https://github.com/shahid129/mycar/issues/7)]

- Login with Facebook
    - As a User I can Login using Facebook so that I can easily create an account (could have / not completed / future feature) [[#8](https://github.com/shahid129/mycar/issues/8)]
- Log in using Google 
    - As a User I can Login using Google so that I can easily create an account (could have / not completed / future feature) [[#9](https://github.com/shahid129/mycar/issues/9)]
- Add Search field
    - As a User I can Search content so that I can find content easily (must have / complete) [[#10](https://github.com/shahid129/mycar/issues/10)]
- Date Time Picker
    - As a User I can easily select/pick a date so that I don't have to write the date manually (must have / complete) [[#11](https://github.com/shahid129/mycar/issues/11)]
- Add Multiple Image
    - As a User I can Upload multiple Images for every post so that others can know more about my post from the image (must have / complete) [[#12](https://github.com/shahid129/mycar/issues/12)]
- User Profile
    - As a user I should have a profile so that I can store my details (must have / complete) [[#13](https://github.com/shahid129/mycar/issues/13)]
- Edit User Profile
    - As a user I can edit my profile so that I can update my details when needed (must have / complete) [[#14](https://github.com/shahid129/mycar/issues/14)]
- About Page
    - As a user I can view the about page so that I know more about the page and find the company's contact details  (must have / complete) [[#15](https://github.com/shahid129/mycar/issues/15)]
-  Post Ad 
    - As a user I can can post my add so that I can sell my cars and add details of my car (must have / complete) [[#16](https://github.com/shahid129/mycar/issues/16)]
- Edit my ad 
    - As a user I can edit my add so that I can change any information when needed (must have / complete) [[#17](https://github.com/shahid129/mycar/issues/17)]
- Delete post
    - As a user I can delete my ad so that it's no longer visible on the page (must have / complete) [[#18](https://github.com/shahid129/mycar/issues/18)]


## Design
The design of the website was made using balsamic wireframes. Each page was created with ideas from the frameworks. Three images are displayed in each wireframe, first one is a laptop, the middle one is a tablet and the last one is a phone.
- Home

![Home](https://res.cloudinary.com/shahid129/image/upload/v1665688036/static/wireframes/home_utbee6.jpg)


- Post Your Add

![Post Your Add](https://res.cloudinary.com/shahid129/image/upload/v1665689144/static/wireframes/post-your-add_edit-post_fg8vga.jpg)

- Post Your Add (Unregistered or not logged in user)

![Post Your Add](https://res.cloudinary.com/shahid129/image/upload/v1665688774/static/wireframes/post-your-add-unregistered-user_xqql98.jpg)

- About

![About](https://res.cloudinary.com/shahid129/image/upload/v1665688036/static/wireframes/about_xprjvo.jpg)

- Login 

![Login](https://res.cloudinary.com/shahid129/image/upload/v1665688036/static/wireframes/login_ipbb4a.jpg)

- Register

![Register](https://res.cloudinary.com/shahid129/image/upload/v1665688036/static/wireframes/register_ogirhx.jpg)

- User Profile

![User Profile](https://res.cloudinary.com/shahid129/image/upload/v1665688036/static/wireframes/user-profile_v1ztor.jpg)

### Color
To maintain the contrast between the foreground and the background of the website, only a few colors were used throughout the page. 

### Main Colors

![main colors](https://res.cloudinary.com/shahid129/image/upload/v1665690491/static/wireframes/main-colors_gfirw3.png)

- #D9391E was used for the logo and mainly hr and underline color to focus on the background and foreground color

- #198754 was used on forms, buttons and hover effects

- #FFFFFF was used for background 

- #000000 was used for text

### Footer colors

![footer colors](https://res.cloudinary.com/shahid129/image/upload/v1665690491/static/wireframes/footer_colors_e8lg2t.png)

- #3B5998 for Facebook background

- #55ACEE for Twitter background

- #DD4B39 for Google background

- #0082CA for Linkedin background

- #0082CA for Github background

### Bootstrap  colors
![bootstrap colors](https://res.cloudinary.com/shahid129/image/upload/v1665691421/static/wireframes/bootstrap_color_rlxabb.png)

- #5BC0DE was used to provide info to the user

- #D9534F was used to provide warning to the user


## Features
## Technology
## Deployment
## Credits
## Acknowledgement