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

### Epic

The epics were created using the milistones on github. Each epic was created and related issues were added to it. A time frame was added to make sure the tasks were done on time. Some of the user stories were left individual. There are four epics - 

- EPIC: CRUD Functionalities

    - USER STORY: Post Ad [[#16](https://github.com/shahid129/mycar/issues/16)]
    - USER STORY: Edit my ad[[#17](https://github.com/shahid129/mycar/issues/17)]
    - USER STORY: Delete post [[#18](https://github.com/shahid129/mycar/issues/18)]
    - USER STORY: Add Multiple Image [[#12](https://github.com/shahid129/mycar/issues/12)]
    - USER STORY: Date Time Picker [[#11](https://github.com/shahid129/mycar/issues/11)]

- EPIC: Register & Login and Logout

    - USER STORY: Email validation on sign up [[#23](https://github.com/shahid129/mycar/issues/23)]
    - USER STORY: Register Account [[#4](https://github.com/shahid129/mycar/issues/4)]
    - USER STORY: Login and Logout [[#2](https://github.com/shahid129/mycar/issues/2)]

- EPIC: User profile 

    - USER STORY: User Profile [[#13](https://github.com/shahid129/mycar/issues/13)]
    - USER STORY: Edit User Profile [[#14](https://github.com/shahid129/mycar/issues/14)]

- Epic: Enable user interaction by providing site pagination, comments, and likes

    - USER STORY: Like a post [[#7](https://github.com/shahid129/mycar/issues/7)]
    - USER STORY: Comments [[#3](https://github.com/shahid129/mycar/issues/3)]
    - USER STORY: Site Pagination  [[#1](https://github.com/shahid129/mycar/issues/1)]

### Product Backlog 

- My Car Product Backlog

    - USER STORY: Reset Password  [[#22](https://github.com/shahid129/mycar/issues/22)]
    - USER STORY: Log in using Google  [[#9](https://github.com/shahid129/mycar/issues/9)]
    - USER STORY Login with Facebook  [[#8](https://github.com/shahid129/mycar/issues/8)]


### User Stories
**USER STORIES ARE EXPLAINED IN DETAILS IN [Testing](#testing) Section**

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
<!-- - CRUD Functionalities
    - As a User I can Create, read, update and delete items so that I have control on my post and contents (must have / complete) [[#6](https://github.com/shahid129/mycar/issues/6)] -->
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

## Testing

Manual testing was conducted for this project and they are as follows:

**User Story 1**
- As a Site User I can View a paginated list of posts so that I can easily select a post to view(must have/ completete) [#1](https://github.com/shahid129/mycar/issues/1)

**Testing steps**

1. Navigate to the home page and scroll to the bottom of the page
2. Click on the button where it says "Next" to go to next page or "Last" to go to the last page

**Expected Results**

1. If you click on the next page, you will be navigated to the next page.
2. If you click on the last page, you be navigatd to the last page and so on

**Actual Results**

1. If you click on the next page, you will be navigated to the next page.
2. If you click on the last page, you be navigatd to the last page and so on

![](https://res.cloudinary.com/shahid129/image/upload/v1666179970/static/testing%20doc/pagination_whggru.png)

**Results: Pass**


**User Story 2**
- As a User I can I can login and logout so that I can access my content (must have/ completete) 
[[#2](https://github.com/shahid129/mycar/issues/2)]

**Login**

**Testing steps**
1. Navigate to the home page and click on Login button on the nav bar
2. You will be brought to the login page
3. Enter your login credentials to log in.

**Expected Results**
1. If you login is successfull, you will be redirected to home page, saying "You are logged in as USERNAME".
2. With an unsucssfull login you will be notified saying "Invalid username or password"
3. You will receive notification stating "Invalid username or password" if your login attempt is unsuccessful.
4. Login button changes to Logout

**Actual Results**
1. If you login is successfull, you will be redirected to home page, saying "You are logged in as USERNAME".
2. With an unsucssfull login you will be notified saying "Invalid username or password"
3. You will receive notification stating "Invalid username or password" if your login attempt is unsuccessful.
4. Login button changes to Logout

- Login is successfull

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666180893/static/testing%20doc/login-successful_jcy0vo.png)

- Login is unsuccessfull

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666180851/static/testing%20doc/login_unsuccess_ppp5ne.png)

**Results: Pass**

**Logout**

**Testing steps**
1. If you are logged in, Click on the log out button in the nav bar to log out

**Expected Result**
1. When you click on the logout button, You will be logged out, with a notification that you are logged out
2. After logout the user is brought back to the home page
3. you get a notification stating "You have successfully logged out"
4. Logout button changes  to Login

**Actual Result**
1. When you click on the logout button, You will be logged out, with a notification that you are logged out
2. After logout the user is brought back to the home page
3. You get a notification stating "You have successfully logged out"
4. Logout button changes  to Login

![](https://res.cloudinary.com/shahid129/image/upload/v1666183460/static/testing%20doc/logout_sb3gqe.png)

**Results: Pass**

**User Story 3**

- As a User I can Comment on a content so that *I can involve in the conversation. (must have/ completete) [[#3](https://github.com/shahid129/mycar/issues/3)]

**Expected Results**
1. Login to your account
2. Navigate to the details of the car
3. On the right bottom of the page users can leave a comment.
4. Once you hit submit, you get a notification stating "Your comment is awaiting
approval"
5. Comment shows in the comment section

**Actual Results**
1. Login to your account
2. Navigate to the details of the car
3. On the right bottom of the page users can leave a comment.
4. Once you hit submit, you get a notification stating "Your comment is awaiting
approval"
5. Wait for admin to approve your comments
6. Comment shows in the comment section

![](https://res.cloudinary.com/shahid129/image/upload/v1666183906/static/testing%20doc/comment-approval_yfms7u.png)

once the comment is approved by admin

![](https://res.cloudinary.com/shahid129/image/upload/v1666183907/static/testing%20doc/after-comment_bijz7z.png)

**Results: Pass**

**User Story 4**
- As an Admin I can access the user comments so that I can remove the inappropriate contents from the page. (must have/ completete)
[#5](https://github.com/shahid129/mycar/issues/5)

**Expected Results**
1. Navigate to the admin page of the website and login using the admin credentials
2. Navigate to customer comments section in the admin panel where you can see all the comments.
3. On the 'Action' tab, from the drop down menu select, approve or delete a comment
4. Click on 'Go' for the relevant action.

**Actual Results**
1. Navigate to the admin page of the website and login using the admin credentials
2. Navigate to customer comments section in the admin panel where you can see all the comments.
3. On the 'Action' tab, from the drop down menu select, approve or delete a comment
4. Click on 'Go' for the relevant action.

![](https://res.cloudinary.com/shahid129/image/upload/v1666184370/static/testing%20doc/admin-comments_ah3dzg.png)

**Results: Pass**


**User Story 5**
- As a User I can Register an account so that I can post my add and comments (must have/ completed)
[[#4](https://github.com/shahid129/mycar/issues/4)]

**Testing Steps**
1. Navigate to the Register page from the nav bar.
2. Enter your Name, email, password to register.

**Expected Results**

1. If username already exists, users need to pick a different username.
2. Email field needs to have a proper email id
3. Passowrds needs to match
4. User will be notified if any of the above details are not correct
5. Upon successfull registration they are redirected to login page with a "Registration successfull" message

**Actual Results**
1. If username already exists, users need to pick a different username.
2. Email field needs to have a proper email id
3. Passowrds needs to match
4. User will be notified if any of the above details are not correct
5. Upon successfull registration they are redirected to login page with a "Registration successfull" message

    - Username already exists
    ![](https://res.cloudinary.com/shahid129/image/upload/v1666185618/static/testing%20doc/registation-1_bgmfuo.png)

    - Email field needs to have a proper email id
    ![](https://res.cloudinary.com/shahid129/image/upload/v1666185618/static/testing%20doc/registation-3_ato4tj.png)

    - Passowrds needs to match
    ![](https://res.cloudinary.com/shahid129/image/upload/v1666185618/static/testing%20doc/registration-2_f6t8f8.png)

    - Successfull registration 
    ![](https://res.cloudinary.com/shahid129/image/upload/v1666185803/static/testing%20doc/registration-successful_sclpgu.png)

**Results: Pass**


**User Story 16**
- As a user I can can post my add so that I can sell my cars and add details of my car (must have/ completed)
[[[#16](https://github.com/shahid129/mycar/issues/16)]


**Testing Steps**
1. Login to the page by putting your log in details
2. Navigate to "Post Your Ad" page
3. All details are mandatory on this page
4. Click Submit on completion of the form

**Expected Results**
1. The user will be taken back to the highlighted area if any fields are left blank or are filled out incorrectly.
2. The user will return to the 'Home' page after uploading something successfully and see the message "Post Successful."

**Actual Results**
1. The user will be taken back to the highlighted area if any fields are left blank or are filled out incorrectly.
2. The user will return to the 'Home' page after uploading something successfully and see the message "Post Successful."

    - Incorrectly filled out form (Highlighted is Model Year in this case)

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666186564/static/testing%20doc/post-add-wrong-1_sxku1a.png)

    - Successful post

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666186564/static/testing%20doc/post-successful_c1zh7t.png)

**Results: Pass**


**User Story 17**
- As a user I can edit my add so that I can change any information when needed (must have/ completed)
[[[#17](https://github.com/shahid129/mycar/issues/17)]

**Testing Steps**
1. Login to the page by putting your log in details
2. Navigate to "Edit" page
3. All details are mandatory on this page


**Expected Results**
1. The user will be taken back to the highlighted area if any fields are left blank or are filled out incorrectly.
2. The user will return to the home page after Editing and updating something successfully and see the message "Updated Successfully."

**Actual Results**
1. The user will be taken back to the highlighted area if any fields are left blank or are filled out incorrectly.
2. The user will return to the home page after Editing and updating something successfully and see the message "Updated Successfully."

    - Incorrectly filled out form (Model Year is Highlighted in this case)

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666186564/static/testing%20doc/post-add-wrong-1_sxku1a.png)

    - Updated Successfully

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666186947/static/testing%20doc/update-add-success_nz0w6o.png)


**User Story 18**
- As a user I can delete my ad so that it's no longer visible on the page (must have/ completed)
[[[#18](https://github.com/shahid129/mycar/issues/18)]

**Results: Pass**

**Testing Steps**
1. Login to the page by putting your log in details
2. Navigate to your relevant post and you will see 'Delete' option

**Expected Results**
1. Once you click 'Delete', a modal will appear asking for confirmation to delete
2. Once you confirm to delete it, it will be deleted
3. You will be redirected to 'Home' page after deletion of a post
4. A message pops up stating 'Deleted Successfully'

**Actual Results**
1. Once you click 'Delete', a modal will appear asking for confirmation to delete
2. Once you confirm to delete it, it will be deleted
3. You will be redirected to 'Home' page after deletion of a post
4. A message pops up stating 'Deleted Successfully'

    - Delete Button

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666187391/static/testing%20doc/delete-1_qe2jpz.png)

    - Delete Modal

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666187390/static/testing%20doc/delete-modal_tf4bad.png)

    - Deleted Message

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666187389/static/testing%20doc/delete-message_qiiubm.png)

**Results: Pass**


**User Story 7**
- As a User I can Like a post and see the number of likes so that I know which posts are popular. (must have/ completed) [[#7](https://github.com/shahid129/mycar/issues/7)]

**Testing Steps**
1. Login to your account
2. Navigate to the details of any car
3. At the bottom of the image there is a 'Love' icon. Click on it to like and unlike

**Expected Results**
1. When the button is liked, it turns red; when it is unliked, it turns lightseagreen. 
2. It also shows the number of likes 

**Actual Results**
1. When the button is liked, it turns red; when it is unliked, it turns lightseagreen. 
2. It also shows the number of likes 

- Unliked post

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666207746/static/testing%20doc/unliked_yglss0.png)

- Liked 

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666207753/static/testing%20doc/liked_d2exl2.png)

**Results: Pass**


**User Story 8**
- As a User I can Login using Facebook so that I can easily create an account
 (could have/ Incomplete) [[#8](https://github.com/shahid129/mycar/issues/8)]

 1. Navigate to login page
 2. Click on login with facebook
 3. Redirected to facebook authorisation for third party app/service
 4. Once confirmed, your account is created and you can login.

 - Facebook login has not been integrated due to project requirements and a lack of time. But this might be a feature in the future.

 **Results: Incomplete**


 **User Story 9**
- As a User I can Login using Google so that I can easily create an account
 (could have/ Incomplete) [[#9](https://github.com/shahid129/mycar/issues/9)]

 1. Navigate to login page
 2. Click on login with google
 3. Redirected to google authorisation for third party app/service
 4. Once confirmed, your account is created and you can login.

- Google login has not been integrated due to project requirements and a lack of time. But this might be a feature in the future.

**Results: Incomplete**


**User Story 10**
- As a User I can Search content so that I can find content easily
 (could have/ completed) [[#10](https://github.com/shahid129/mycar/issues/10)]

**Testing Steps**
1. Navigate to the search bar in the nav nar
2. Type the key or the name of the car that you want to search for and hit the search button

**Expected Results**
1. A new page appears with the search result
2. The page must show number of search results
3. When you click on the search result, you are redirected to the details of that car

**Actual Results**
 1. A new page appears with the search result
2. The page must show number of search results
3. When you click on the search result, you are redirected to the details of that car

 - Number of cars found

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666208905/static/testing%20doc/search-1_cspuel.png)

- Search results

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666208906/static/testing%20doc/search-2_zu6pcd.png)


**User Story 11**
- As a User I can easily select/pick a date so that I don't have to write the date manually
 (must have/ completed) [[#11](https://github.com/shahid129/mycar/issues/11)]

**Results: Pass**


 **Testing Steps**
 1. Whenever the page asks you to input a date, the page will give you a clickable option to pick a date
 2. Navigate to post your ad
 3. Scroll down to 'Model year', 'NCT Expiry' or 'Tax Expiry'
 4. Click on the widget for a pop-up date picker and pick your desired date

**Expected Results**
 1. A calender pops up when you click the widget
 2. Once you selec the date, it adds to the form

**Actual Results**
1. A calender pops up when you click the widget
2. Once you selec the date, it adds to the form

 - Clickable date picker

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666209492/static/testing%20doc/date-picker-1_sdpnmj.png)

- Date Picker

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666209493/static/testing%20doc/date-picker-2_dxomaf.png)

**Results: Pass**


**User Story 12**
- As a User I can Upload multiple Images for every post so that others can know more about my post from the image
 (must have/ completed) [[#12](https://github.com/shahid129/mycar/issues/12)]

**Testing Steps**
 1. Navigate to post your ad page.
 2. The first image on the top is the profile image of the car
 3. You can upload another three images for the car, which is located at the bottom of the page
 4. Click'submit' to upload your post. The post is available to view on the home page

**Expected Results**
1. Click on the relevant post to view uploaded images.
2. Images appear in a carosel

**Actual Results**
1. Click on the relevant post to view uploaded images
2. Images appear in a carosel

- Multiple images upload (Because images are uploaded in a bootstrap carousel, multiple images cannot be captured)

![](https://res.cloudinary.com/shahid129/image/upload/v1666210032/static/testing%20doc/multi-images_t8dkpk.png)

**Results: Pass**

**User Story 13**
- As a user I should have a profile so that I can store my details
(must have/ completed) [[#13](https://github.com/shahid129/mycar/issues/13)]

**Testing Steps**
1. Login to the page and navigate to the user profile from the top
2. A user is able to upload a profile picture

**Expected Results**
1. A user profile is created automatically when the account is created
2. The page indicates "none" to all of the details for a new user because no information about the user has yet been submitted.


**Actual Results**
1. A user profile is created automatically when the account is created
2. The page indicates "none" to all of the details for a new user because no information about the user has yet been submitted.

- User prorile

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666210924/static/testing%20doc/user-profile_gi2ycj.png)

**Results: Pass**


**User Story 14**
- As a user I can edit my profile so that I can update my details when needed
(must have/ completed) [[#14](https://github.com/shahid129/mycar/issues/14)]

**Testing Steps**
1. Login to the page and navigate to the user profile from the top
2. At the bottom of the page, click 'Edit Details'
3. Fill up the form and hit 'Update Profile'

**Expected Results**
1. The profile is updated and you are redirected to 'Pofile' page
2. A message appears stating that 'Profile updated successfully.'

**Actual Results**
1. The profile is updated and you are redirected to 'Pofile' page
2. A message appears stating that 'Profile updated successfully.'

- Profile Edit page

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666211456/static/testing%20doc/user-profiel-update-form_jgaebu.png)

- Profile updated successfully

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666211456/static/testing%20doc/Profile_updated_successfully._e3gggy.png)

**Results: Pass**

**User Story 15**
- As a user I can view the about page so that I know more about the page and find the company's contact details (must have/ completed) [[#15](https://github.com/shahid129/mycar/issues/15)]

**Testing Steps**
1. Navigate to the 'About' page from the nav bar

**Expected Results**
1. About page shows up with all the detail abou the company
2. The main sections of this page are "Mission," "Your privacy," and "Contact us." 
3. Users hover on any of the section and details of that section shows up

**Actual Results**
1. About page shows up with all the detail abou the company
2. The main sections of this page are "Mission," "Your privacy," and "Contact us." 
3. Users hover on any of the section and details of that section shows up

- Hover effect on a section

    ![](https://res.cloudinary.com/shahid129/image/upload/v1666215467/static/testing%20doc/about-hover_khnaec.png)

**Results: Pass**


**User Story 22**
- As a User I can reset my password so that I not logged out of my account permanently
(coul have/ Incompleted) [[#22](https://github.com/shahid129/mycar/issues/22)]

    - Incomlete as this was not a mandotory section for this project and the time frame was limited 

**Results: Incomplete**

**User Story 23**
- As a User I can receive an email so that I can validate my account sign up (should have/ completed) [[#15](https://github.com/shahid129/mycar/issues/23)]

**Testing Steps**
1. Navigate to the 'Register' page
2. Fill up the required details
3. Click 'Register' button and check your email for a verification email

**Expected Results**
1. An email has been sent your email with a verification link
2. Once you click on the link, you are brought back to the login page 
3. Enter your details and log in

**Actual Results**
1. An email has been sent your email with a verification link
2. Once you click on the link, you are brought back to the login page 
3. Enter your details and log in

- Email confirmation
    ![](https://res.cloudinary.com/shahid129/image/upload/v1666555108/static/testing%20doc/email-verification_vzfgyy.png)

- Click email link 
    ![](https://res.cloudinary.com/shahid129/image/upload/v1666555109/static/testing%20doc/email-verification-2_czlsvq.png)

**Results: Pass**


## Testing Features

### Logo
**Testing Steps**
1. Click on the logo
2. Navigate to different page and click on the logo

**Expected Results**
1. Logo links back to home page from any other pages

**Actual Result Results**
1. Logo links back to home page from any other pages

**Results: Pass**

### Footer
**Testing Steps**
1. Click on any icon on the footer
2. Navigate to different page and and follow step 1

**Expected Results**
1. Each icon opens in a different tab
2. Each icon opens the right page when clicked

**Actual Result Results**
1. Each icon opens in a different tab
2. Each icon opens the right page when clicked

**Results: Pass**

### Navigation and Button
Check all navigation if they are working as expected

### Home
**Testing Steps**
1. Click on the Home
2. Navigate to different page and click on the Home

**Expected Results**
1. Home links back to home page from any other pages
2. Home button is only vissible to everyone

**Actual Result Results**
1. Home links back to home page from any other pages
2. Home button is only vissible to everyone

**Results: Pass**

### Post Your Ad
**Testing Steps**
1. Click on the Post Your Ad
2. Navigate to different page and click on the Post Your Ad

**Expected Results**
1. Post Your Ad links back to Post Your Ad page from any other pages
2. Post Your Ad button is only vissible to everyone
3. Only logged in users can make a post

**Actual Result Results**
1. Post Your Ad links back to Post Your Ad page from any other pages
2. Post Your Ad button is only vissible to everyone
3. Only logged in users can make a post

    ![](https://res.cloudinary.com/shahid129/image/upload/v1665836381/static/documents/post-ad-not-logged_l5wb6z.png)

**Results: Pass**

### About
**Testing Steps**
1. Click on the About
2. Navigate to different page and click on the About

**Expected Results**
1. About links back to About page from any other pages
2. Post Your Ad button is only vissible to everyone

**Actual Result Results**
1. About links back to About page from any other pages
2. Post Your Ad button is only vissible to everyone

**Results: Pass**

### Login
**Testing Steps**
1. Click on the Login
2. Navigate to different page and click on the Login

**Expected Results**
1. Login links back to Login page from any other pages
2. User logs in 
3. Hide login button
4. Show logout button
5. Hide register button

**Actual Result Results**
1. Login links back to Login page from any other pages
2. User logs in 
3. Hide login button
4. Show logout button
5. Hide register button

    ![](https://res.cloudinary.com/shahid129/image/upload/v1665775651/static/documents/nav-signed-in_jwbcko.png)

**Results: Pass**

### Logout
**Testing Steps**
1. Click on the Logout
2. Navigate to different page and click on the Logout

**Expected Results**
1. Logout links back to Logout page from any other pages
2. User logged out 
3. Show login button
4. Hide logout button
5. Show register button

**Actual Result Results**
1. Logout links back to Logout page from any other pages
2. User logged out 
3. Show login button
4. Hide logout button
5. Show register button

![](https://res.cloudinary.com/shahid129/image/upload/v1665775651/static/documents/nav-not-signed-in_rjqps6.png)

**Results: Pass**

### Register
**Testing Steps**
1. Click on the Register
2. Navigate to different page and click on the Register

**Expected Results**
1. Register button is only vissible to not logged in users
2. Register links back to Register page from any other pages

**Actual Result Results**
1. Register button is only vissible to not logged in users
2. Register links back to Register page from any other pages

**Results: Pass**

### Search
**Testing Steps**
1. Click on the Search
2. Navigate to different page and click on the Search

**Expected Results**
1. Search button is only vissible to everyone
2. Type any key and hit search
3. Show results of searched car

**Actual Result Results**
1. Search button is only vissible to everyone
2. Type any key and hit search
3. Show results of searched car

**Results: Pass**

### View Cars Button
**Testing Steps**
1. Navigate to Home and click on the View Cars

**Expected Results**
1. The View Cars button brings you to the relevant section for car ads.

**Actual Result Results**
1. The View Cars button brings you to the relevant section for car ads.

**Results: Pass**



### Image button to view car details
**Testing Steps**
1. Navigate to Home and click on the image

**Expected Results**
1. You will be redirected to the post details page to view the relevant car

**Actual Result Results**
1. You will be redirected to the post details page to view the relevant car

**Results: Pass**




## Technology

### Languages 

- [HTML5](https://en.wikipedia.org/wiki/HTML)
    was used build core front end of the website.

 - [CSS](https://en.wikipedia.org/wiki/CSS)
    was used to add style to html and responsivenes

- [JavaScript](https://www.javascript.com/)
    was used to add one or a few interactivities to the page. It was used mainly with bootstrap to add interactivity to the front end
- [JQuery](https://jquery.com/)
    was used to add interactivity to the page

 - [Bootstrap 5](https://getbootstrap.com/)
    was used throughout to add interactivity, style, and responsiveness to the page.

- [Python](https://www.python.org/) 
    was used to code the backend of the project
    

### Frameworks

- [Django 3.2.15](https://www.djangoproject.com/)
    was used throughout the project along with its supporting libraries

- Supporting libraries - 

    - [crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
        was used to add style to django forms

    - [summernote](https://summernote.org/) 
        as a editor 

    - [psycopg2](https://www.psycopg.org/docs/)
        as a database adaptor for python PostgreSQL databases

    - [gunicorn](https://gunicorn.org/) 
        as a server for heroku

    - [django active link](https://pypi.org/project/django-active-link/)
        was used to highlight active links in your Django app.

    - [pillow](https://pypi.org/project/Pillow/)
        was used as python imaging library
### Database 
- Heroku Postgres was used for the production database

- SQLite3 was used for automated testing in the local environment

### Other Technologies

- [Gitpod](https://www.gitpod.io/) - as the IDE
- [Cloudinary](https://cloudinary.com/) - to host static files
- [Git](https://git-scm.com/) - as a version control
- [Github](https://github.com/) - to store code in the repository
- [Heroku](https://www.heroku.com/) - to deploy on a cloud based platform
- [Google Chrome](https://www.google.com/chrome/?brand=CHBD&brand=CHBD&gclid=EAIaIQobChMIxrSx5p_o-gIVE-vtCh3qvA4EEAAYASABEgIB0vD_BwE&gclsrc=aw.ds) - web browser
- [Google Fonts](https://fonts.google.com/)  - for the fonts
- [Google Sheet](https://www.google.com/sheets/about/) - to create tables for db model
- [Fontawesome](https://fontawesome.com/) - for icons
- [Favicon](https://favicon.io/) - to create the favicon
- [Balsamic](https://balsamiq.com/) - to create the wireframes
- [Coolors](https://coolors.co/) - to create the color palate
- [Compressor](https://compressor.io/) - to compress the image
- [W3C Markup Validation Service](https://validator.w3.org/) - to validate html
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - to validate css
- [PEP8](https://peps.python.org/pep-0008/) - to validate python code

## Deployment

### Create app in django
Type the codes in the terminal in the following series of process

- Install Django and gunicorn: `pip3 install django gunicorn` 

- Install database libraries dj_database_url and psycopg2 library: `pip3 install dj_database_url psycopg2`

- Install Cloudinary libraries to manage photos: `pip3 install dj-3-cloudinary-storage`

- Create file for requirements file: `pip freeze --local > requirements.txt`

- Create your project: `django-admin startproject your_project_name .`

    - Do not miss the dot '.' in the end

- Create your app: `django-admin startapp your_app_name`

- Make migrations: `python3 manage.py makemigrations`

- Migrate changes: `python3 manage.py migrate`

- Run the server to test if the app is installed: `python3 manage.py runserver`


### Heroku

- To create your heroku app

    - Navigate to the Heroku website

    - Create an account by entering your email address and a password (log in if you already have an account)

    - Use the authentication email that was sent to your email account to activate the account

    - Choose "create a new app" from the dropdown menu by clicking the "new" button

    - Give the application a name; it must be unique; in this case, the app is called "MyCar"

    - Select a region, in this case Europe

    - Click create app

- Create the database

    - Click on the newly created app

    - Navigate to heroku dashboard and click "Resources" button

    - Scroll down to Add-Ons, search for and select 'Heroku Postgres'

    - In the Settings tab, scroll down to 'Reveal Config Vars' and copy the text in the box beside DATABASE_URL (you will need this in the next step)

- Set up Environment Variables

    - Create a new env.py file in the root directory of Gitpod

    - To the .gitignore file, add env.py

    - Import the os library into env.py: `import os`

    - In env.py add `os.environ["DATABASE_URL"] = "Paste in the text link copied`

    - Go back to heroku settings and click reveal config vars

    - Paste the 'SECRET KEY' in the secret key box

- Connect the environment variables to Django

    - Go to 'settings.py' file in Django and add the code:

            from pathlib import Path
            import os
            import dj_database_url
            if os.path.isfile('env.py'):
                import env
    - Remove the default insecure secret key in settings.py and replace with the link to the secret key variable i Heroku by typing: `SECRET_KEY = os.environ.get(SECRET_KEY)`

    - Comment out the DATABASES section in settings.py 

    - And add the following 

            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': BASE_DIR / 'db.sqlite3',
                }
            }

    - Make the migrations

        `python3 manage.py makemigrations`

        `python3 manage.py migrate`


- Set up Cloudinary for static and media files storage

    - Navigate to cloudinary page, signin or create an account

    - Go to your cloudinary account and from the 'Dashboard' in Cloudinary copy your url into the env.py file by typing: `os.environ["CLOUDINARY_URL"] = "cloudinary://<insert-your-url>"`

    - Go to Heroku and add add cloudinary url to 'config vars'

    - Add DISABLE COLLECTSTATIC with a value of "1" to the Heroku configuration variables (note: this must be removed for final deployment)

    - In the following order, add the Cloudinary libraries to the Django settings.py section for installed apps:

            'cloudinary_storage'
            'django.contrib.staticfiles''
            'cloudinary'

    - Add the follwing in settings.py to connect cloudinary to Django

            STATIC_URL = '/static/'
            STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
            STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
            STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

            MEDIA_URL = '/media/'
            DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

    - Link file to the templates directory in Heroku 

    - Add this under the BASE_DIR: `TEMPLATES_DIR = os.path.join(BASE_DIR,
    'templates')`

    - Change the templates directory to TEMPLATES_DIR. Add this within the TEMPLATES array: `'DIRS': [TEMPLATES_DIR]`

    - To ALLOWED_HOSTS Add Heroku Hostname: `ALLOWED_HOSTS = ['shahid-my-car.herokuapp.com', 'localhost']`

- Create three folders in the root directory media, static and templates

- Create Procfile in the root directory

- In the Procfile add: `web: gunicorn favoureats .wsgi`

- In terminal add, commit, and push:
    
    - add to add items

    - commit - to add short messages

    - push - to push it to github

            git add <filename>
            git commit -m “Deployment Commit”
            git push

- Deployment to Heroku

    - Go to heroku and click on your app

    - Click 'Deploy' and scroll down to 'Deployment method' section

    - Select 'Github' and click the 'connect to Github' button to confirm

    - Enter the project's Github repository name in the search field

    - In order to connect the Heroku app and the Github repository, first click search and then click connect
    - Once connected the display will show that Heroku is linked to the repository

- Final Deployment

    - Upon completion of development, change the debug setting to: In settings.py: `DEBUG = False`

    - In order for this project's use of the Summernote editor to function in Heroku, add the following line to settings.py: `X FRAME OPTIONS = "SAMEORIGIN"`

    - In Heroku settings config vars change the DISABLE_COLLECTSTATIC value to 0

    - It is advised that only manual deployment be used in Heroku since DEBUG must be set to 'True' for development and 'False' for production

    - 'Choose a branch to deploy' should be 'main'

    - To manually deploy click the button 'Deploy Branch'

    - Your app was successfully deployed will be displayed when the app is deployed. 

    - The deployed app will appear in the browser after you click "view."


### Local Deployment

- Forking the Repository

    - To fork the project navigate to the mycar repository at https://github.com/shahid129/mycar

    - Click on the drop down menu CODE

    - Choose the https option, then copy the link

    - Open the terminal

    - Change the location of the current working directory to the desired destination

    - At the top right of the page, select "Fork" 
    
    - The repository's forked version will show up in your Repositories tab.


- Cloning Repository

    - To fork the project navigate to the mycar repository at https://github.com/shahid129/mycar

    - Click on the drop down menu 'Code'

    - Choose the https option, then copy the link

    - Open the terminal

    - Change the location of the current working directory to the desired destination

    - Type the git clone command with the copied URL

            git clone https://github.com/shahid129/mycar.git
    - To build the local clone, press enter

    - As mentioned above in 'Set up Environment Variables' an env.py file needs to be created in order for the project to start. This won't be copied along with the other files because it isn't kept on Github.




## Credits
## Acknowledgement