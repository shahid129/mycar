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

### Data Models
There are four data models in this project. PostAd model, Customer Comment model, Images model and a User Profile model. User profile model is in a separate app inside the project. 

- PostAd model

![PostAd model](https://res.cloudinary.com/shahid129/image/upload/v1665750792/static/wireframes/model-post-ad_izkocl.png)

- Customer Comment model

![Customer Comment model](https://res.cloudinary.com/shahid129/image/upload/v1665750792/static/wireframes/model-customer-comment_wlitup.png)

- Images model

Images model was created because I wanted give the opportunity to the user to upload multiple images.

![Images model](https://res.cloudinary.com/shahid129/image/upload/v1665750791/static/wireframes/model-images_xaniwl.png)

-  User Profile model

The user Profile model was created so that the user can have a profile of their own when they sign up for the website. I could have put the User Profile model in the same app, but I wanted to create a new app for the user model so that everything does not jumble up too much and looks cleaner.

![ User Profile model](https://res.cloudinary.com/shahid129/image/upload/v1665750792/static/wireframes/model-user-profile_eaehps.png)

## Features
The planning and execution of this project were a vital part of the project. You need to know exactly what you want to have in your project. The main objective of this project was to allow the users to have CRUD functionalities where they can post an ad, and edit and delete it. To allow them to have CRUD functionalities they needed to create an account. In addition to these some extra features have also been added to the project, like search cars and user profiles. This makes the website looks complete. The main pages of the websites are Home, Post Your Ad, About, Login, and Register. When the user logs in there is another option User's Profile.

### Logo

- The logo for the website is simply the name of the website "MyCar". The logo has a hover effect, when you hover on it the vermillion color of "Car" turns to balck and black color of "Car turns to vermillion. Jquery was used to enable this effect.
![](https://res.cloudinary.com/shahid129/image/upload/v1665774682/static/documents/logo_k10jr3.png)

### Nav Bar

- The nav bar when user is not signed in.
![](https://res.cloudinary.com/shahid129/image/upload/v1665775651/static/documents/nav-not-signed-in_rjqps6.png)


- The nav bar changes when a user is signed in. A logout button replaces the login button and a user's profile button replaces the register button.
![](https://res.cloudinary.com/shahid129/image/upload/v1665775651/static/documents/nav-signed-in_jwbcko.png)

- Nav bar on small device 
![](https://res.cloudinary.com/shahid129/image/upload/v1665776050/static/documents/nav-small-device-collapse_ds1zpj.png)

- Nav bar on small device when it is clicked 
![](https://res.cloudinary.com/shahid129/image/upload/v1665776050/static/documents/nav-small-device-open_mnlcwo.png)

- There is also active status on the nav bar. A small vermillion dot appears under the name of the nav bar, which ensures the user which page they are on.

### Home Page

- Hero Image 
    - Hero Image represents the purpose of the website showing car images with the heading Find Your Perfect Car. Opacity is added to the hero image to make the text clear out. The "View Car" button scrolls smoothly to the cars ad section. Anyone visiting the website can view cars.

- Latest Cars

    The pages are fully responsive, thus the layout of the page changes depending on user's device. Significant information about the car is available to see on the main page. A user can get the full details of a car by clicking on the image.

    - Laptop View
        
        Six car ad is the maximum number that can appear on a page. Hence it is broken down to two lines of three.
        ![](https://res.cloudinary.com/shahid129/image/upload/v1665777741/static/documents/latest-car-laptop_jbl0kv.png)

    - Tablet View

        Posts appear in two columns on the tablet view
        ![](https://res.cloudinary.com/shahid129/image/upload/v1665777360/static/documents/latest-car-tablet_jqbz92.png)
    
    - Mobile View 

        On a smaller device a single post appears.

        ![](https://res.cloudinary.com/shahid129/image/upload/v1665777359/static/documents/latest-car-mobile_pvdssm.png)


    - Signed in user

        When a user is signed in and has a post, the page recognises the user and his relevant ads, and gives him the option to "Edit" or "Delete" the post.
        ![](https://res.cloudinary.com/shahid129/image/upload/v1665777742/static/documents/latest_car_logged_in_ujfyhd.png)

### Post Detail Page

- Image Carousel

    Once the user clicks on an ad and goes to the post detail page, an image carousel appears with the images they uploaded when making the post. Three images are layered on top of each other using the bootstrap carousel.

    ![](https://res.cloudinary.com/shahid129/image/upload/v1665785729/static/documents/carosel_wdwz0c.png)

- Like an Ad and Comment

    Users can like and unlike a post. When users like a post the icon changes to vermillion showing number of likes 

    The number of comments shows on the right of the comment icon.
    ![](https://res.cloudinary.com/shahid129/image/upload/v1665785828/static/documents/like-comment_nwsxfb.png)

- Unlike an Ad and no comment
    When there is no like on a post the like count shows zero with its base color lightseagreen

    When there is no comment on a post the comment count shows zero with its base color lightseagreen

    ![](https://res.cloudinary.com/shahid129/image/upload/v1665785829/static/documents/no-likes-no-coment_vg40mn.png)

- Key info and detail info

    Three key facts about a car are represented by key info. The year indicates the year the car was manufactured. Road tax is the road tax's expiration date, and NCT expiry informs you of the NCT expiration date. (The terms used here are based in Ireland; they may vary in other nations.)

    You can get more particular information by looking at detailed information. The car's official pages provide comprehensive information. For instance, information on Mercedes was obtained from the official Mercedes website.

    ![](https://res.cloudinary.com/shahid129/image/upload/v1665786270/static/documents/info_hlcv6a.png)

- Comment

    Django was used to create a couple of features in the comment section. If no comments have been made, the page displays "Be the first to comment." If there is a comment, the page displays the number of comments, the author's name, the date and time, and the comment.

    - Without comment
    ![](https://res.cloudinary.com/shahid129/image/upload/v1665831407/static/documents/before-comment_zvnyqe.png)

    - With comment 
    ![](https://res.cloudinary.com/shahid129/image/upload/v1665831407/static/documents/after-comment_s8ai1z.png)

    To leave a comment on a post, the user must first create an account and be logged in. Unregistered users are not permitted to leave comments on posts.

    - Not logged in users
    ![](https://res.cloudinary.com/shahid129/image/upload/v1665833844/static/documents/not-logged-in_afay5w.png)

    - Users who are logged in can comment on a post. Additionally, when a user posts a comment, their name is displayed.: User's Name
    ![](https://res.cloudinary.com/shahid129/image/upload/v1665833844/static/documents/logged-in_uudgjg.png)

    - Comment Approval
    The user receives a pop-up notification after leaving a comment that reads, "Your comment is awaiting approval." This notifies the user that their remark was accepted while also retaining the admin's right to accept or reject a comment. This prevents other users from posting offensive comments on the page. Following admin approval, the comment appears in the comment section.
    ![](https://res.cloudinary.com/shahid129/image/upload/v1665834289/static/documents/comment-approval_hdfmyq.png)


## Post Your Ad Page

If a person is logged in, they can create a post to sell their car on the Post Your Ad page. If a user is not signed in, he will be prompted to create an account or, if he already has one, to log in.

- User not logged in 

    ![](https://res.cloudinary.com/shahid129/image/upload/v1665836381/static/documents/post-ad-not-logged_l5wb6z.png)

- Logged in user

    Users must complete the form with all required fields (All fields are required). The first image is a profile of the car, while the other three are supplemental images.

    ![](https://res.cloudinary.com/shahid129/image/upload/v1665836380/static/documents/post-ad-logged-in_gkjlok.png)

    - If the user provides incorrect information, feedback is provided to the user. In this situation, the user was intended to enter numbers rather than letters into the supplied field.

        ![](https://res.cloudinary.com/shahid129/image/upload/v1665836919/static/documents/post-ad-1_hddohi.png)

    - If there is an empty field left on the form, the user gets a pop-up message to "Please fill in this field."

        ![](https://res.cloudinary.com/shahid129/image/upload/v1665837117/static/documents/post-ad-2_vnxo22.png)

    - If an image field is left blank, the user is brought back to the image field, which is highlighted with a light sea green color.

        ![](https://res.cloudinary.com/shahid129/image/upload/v1665837479/static/documents/post-ad-3_hwjgpy.png)

    - The user is not allowed to have a post title with the same name as one that already exists.

        ![](https://res.cloudinary.com/shahid129/image/upload/v1665837681/static/documents/post-ad-4_krrcya.png)

    - When all fields are correctly filled out and the post is successful, the user is redirected to the home page with the message "Post was successful."
        ![](https://res.cloudinary.com/shahid129/image/upload/v1665838018/static/documents/post-successful_tbunmq.png)

## Post Your Ad Edit Page

- Users that are logged in can only make changes to their ad. On their ad, an edit and delete button will appear, giving them the opportunity to either edit or delete their ad. When they click the edit button, the edit page with all of the formatting fields from their original post will appear.

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666033830/static/documents/Screenshot_2022-10-17_at_20.03.35_wu7u8p.png)

- When the user hits "Update" after altering all of the details, the form updates itself along with the database and returns them to the home page. A message appears on the home page that says "Update Successful."

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666034059/static/documents/Screenshot_2022-10-17_at_20.11.26_hmutwa.png)

## About Page

- The About page contains information about the website and the company. Anyone who has internet connection is able to see this page. A brief overview of the company is followed by three important features of the company, namely Mission, Privacy, and Contact Us. 
    ![](https://res.cloudinary.com/shahid129/image/upload/v1666034615/static/documents/about_wye2ow.png)

- JQuery is used to add a hover effect to this page. When a user hovers their cursor over one of the primary aspects, the column softly expands out to show a description of it.

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666034712/static/documents/about-hover_yi7xf4.png)

## User's Profile

- Every time a user registers themselves, a user profile is created. They will have the chance to see their profile and alter any changes to their details after they have logged in. This is entirely up to the user and is optional. A user is also permitted to add their profile picture and certain essential data.

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666035697/static/documents/user-profile_edttpq.png)

- Additionally, users can view their most recent login date and time.
    ![](https://res.cloudinary.com/shahid129/image/upload/v1666035391/static/documents/profile-last-login_qvbajz.png)

- A user can edit their profile and update anything they wish to. All fields are prepopulating from their original post

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666035925/static/documents/user-profile-edit_yjqsev.png)

- When the user hits "Update" after altering all of the details, the form updates itself along with the database and returns them to the home page. A message appears on the home page that says "Profile Update Successful."

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666036046/static/documents/profile-updating_osn6sk.png)

## Search Bar

- Users can easily search for any cars using the search bar that is available. Anyone can visit the search bar and look for cars there. The title name of the cars will be used to search for matched vehicles. Any close match to the search title will seek for cars and display on the page; exact matches are not required.

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666036482/static/documents/search_josuz5.png)

- The names of the cars and their primary images are displayed alongside the search results on a well-structured page. It also indicates how many results were found after a search and what was being looked for. When the user clicks on the search result, it brings them to the relevant page.

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666037271/static/documents/search-result_swgfsa.png)

- Login

   - A user can log in by providing their name and password if they are already registered.
Unregistered users can access the registration page by clicking the "register" button, which will take them there.

        ![](https://res.cloudinary.com/shahid129/image/upload/v1666037876/static/documents/sign-in_f2gp4q.png)
    
    - After successfully logging in, the user is returned to the home page and is given the message "You are logged in as USERNAME."
        ![](https://res.cloudinary.com/shahid129/image/upload/v1666038457/static/documents/login-successful_fii6yo.png)

- Registration

    - By entering their name, email address, and a password of their    choice, users can register for an account. They click the sign in   button to access the sign in page if they already have an account.

        ![](https://res.cloudinary.com/shahid129/image/upload/v1666038233/static/documents/registration_inhbjf.png)
    
    - The user is taken back to the login page after registering successfully and is greeted with the message "Registration successful."

        ![](https://res.cloudinary.com/shahid129/image/upload/v1666038764/static/documents/registration-successful_fov7ja.png)

- Logout

    The user is promptly logged out and returned to the home page after clicking the logout button, along with a message stating, "You have successfully logged out."

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666039021/static/documents/log-out_dhszbs.png)


## FUTURE FEATURES
The website is always being improved. There is always something interesting and novel to do. Despite the fact that my site may benefit from some more features to liven it up, some of them are listed below.

- At the moment, only a user can CRUD and sell a car, but there is no option for buyers to purchase a car. In the future, a buyer can add an item to the basket and make a purchase with their credit card or cash in hand.

- Payment with paypal can also be added in the future

- No one can now message a seller about the car, but that option could be added in the future so that anyone who wants more information can do so.

- There is no "forget password" option at the minute. Forgetting your password and resetting your password are very important for a well defined webpage. That feature is a must in the future.

- The home page's vehicle advertisement might have a tiny pop-up button added to it. So, when a user clicks on it, a pop-up window displaying all the important details about the car.

- Giving more flexibility to users by allowing them to edit their comments, At the same time, it will show the original comments and edited comments.


## Technology
## Deployment
## Credits
## Acknowledgement