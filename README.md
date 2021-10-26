# Instaclone
## Author
Roy Rasugu

## Description
This is an instagram clone web application that allows us to post pictures, like other people's pictures, follow people and so on.

## Screenshot
<img src="https://github.com/RoyRasugu/Mygallery2.0/raw/master/instagram_clone/static/img/Edit_profile.jpg">
<br>
<br>
<img src="https://github.com/RoyRasugu/Mygallery2.0/raw/master/instagram_clone/static/img/After_edit_profile.jpg">
displays first name,last name and bio.
<br>
<br>
<img src="https://github.com/RoyRasugu/Mygallery2.0/raw/master/instagram_clone/static/img/follow.jpg">
when you click on username of user it takes you to profile where you can follow them if you have not.
<br>
<br>
<img src="https://github.com/RoyRasugu/Mygallery2.0/raw/master/instagram_clone/static/img/unfollow.jpg">
After you follow user the follow button changes from follow to unfollow.
<br>
<br>
<img src="https://github.com/RoyRasugu/Mygallery2.0/raw/master/instagram_clone/static/img/home_post.jpg">
After you follow a user you can see their posts on the home page.
<br>
<br>
<img src="https://github.com/RoyRasugu/Mygallery2.0/raw/master/instagram_clone/static/img/post_details.jpg">
When you like the image on the homepage or click on the image, it takes you to the post details page where can comment on the post, like or unlike and save or remove the post.
<br>
<br>
<img src="https://github.com/RoyRasugu/Mygallery2.0/raw/master/instagram_clone/static/img/save_post.jpg">
This is the save post button
<br>
<br>
<img src="https://github.com/RoyRasugu/Mygallery2.0/raw/master/instagram_clone/static/img/remove_post.jpg">
After you have saved the post the icon changes to remove post.
<br>
<br>
<img src="https://github.com/RoyRasugu/Mygallery2.0/raw/master/instagram_clone/static/img/saved_post.jpg">
The saved post will be displayed on you're profile with on the saved post tab.
<br>
<br>
<img src="https://github.com/RoyRasugu/Mygallery2.0/raw/master/instagram_clone/static/img/search_for_user.jpg">
When you click the inbox link where you can reply to message in the middle or write a new message
<br>
<br>
<img src="https://github.com/RoyRasugu/Mygallery2.0/raw/master/instagram_clone/static/img/search_user.jpg">
when you click the new message button, it directs you here to search for a user
<br>
<br>
<img src="https://github.com/RoyRasugu/Mygallery2.0/raw/master/instagram_clone/static/img/send_message.jpg">
When you click the send message it will send an automatic message "Says hello!" as shown below
<br>
<br>
<img src="https://github.com/RoyRasugu/Mygallery2.0/raw/master/instagram_clone/static/img/message.jpg">
<br>
<br>
<img src="https://github.com/RoyRasugu/Mygallery2.0/raw/master/instagram_clone/static/img/notification.jpg">
When you click the notifications when there are notfications it should display like this.
<br>
<br>
<img src="https://github.com/RoyRasugu/Mygallery2.0/raw/master/instagram_clone/static/img/view_tag.jpg">
This is the tag.
<br>
<br>
<img src="https://github.com/RoyRasugu/Mygallery2.0/raw/master/instagram_clone/static/img/tag.jpg">
The tag page with all images related to the tag.
<br>
<br>
<img src="https://github.com/RoyRasugu/Mygallery2.0/raw/master/instagram_clone/static/img/Follow_function.jpg">
The follow function does not work well so one has to type the username on the url eg eg https://theinstaclone.herokuapp.com/Roy.
<br>
<br>

## Livepage
[livelink](https://instprat.herokuapp.com/)

## Setup Requirements
* Django
* Python

## Setup Installation
* Copy the github repository url
* Clone to your computer
* Open terminal and navigate to the directory of the project you just cloned to your computer
* Run the following command to start the server using virtual environment
python3.8 -m venv --without-pip virtual
* To activate the virtual environment
source virtual/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python
* To run the server

* python manage.py runserver

## Technologies Used
* HTML
* CSS
* Bulma
* Python
* Django

## Dependencies

1. The first thing one views whwn they access the page is the login page as not all users are new users and if they are already registered they will login. If not then they will have to register by pressing the ```create an account``` button.
2. After the user has finished off with the authentication, they will view the home page where they will see posts of already existing users.
3. Here in the post they will see the image posted, the user's first and last name(that is if they have put those details in their profile otherwise it reads no name), caption of the post, like icon with the number of likes and the date and time when the post was posted.
4. One can be able to like the post they've seen in the homepage and they will see the likes increase by one from the initial count. If one hits the like icon again it will unlike the post. the if they click it again it will like again and vice versa.
5. Another functionality is to view one's post in a bigger resolution as they click the image. Once one does this it will redirect them to the post details page where they will see the image bigger than in the homepage, user's credentials who posted the post, date and time when the post was posted and the likes.
6. The new additional things here in the post details page are the ```save post icon```, comment box together with an image box which is the profile picture for the one commenting on the post with a post comment button.
7. Once one comments, the comment will appear below the post with the user's name who commented, the duration when the comment was posted with the user's profile image on the post.
9. The save post icon once clicked, automatically save that post on you're profile where one will see the saved post on the saved tab. Then the page refreshes and the ```save post icon``` now changes to a ```remove post icon```. Then if one clicks the ```remove post```, it removes the saved post from saved tab.
10. The navbar has a profile link which has a profile icon with the username of the user currently logged in. Here in the profile page one will view their username with an '@' before their name, a circular icon for their profile picture, the number of ```posts```, ```following``` and ```followers``` with values of zero. Every time the user adds a post, follows another user or gets a follower, they will increment by one and be displayed as their stats are updated.
11. Then there is the ```edit profile``` button where one chooses their profile picture or change it, put their first name, last name, location and bio.
12. Once the user presses the ```update``` button it will take them back to the homepage as it has saved your details. To view the reflected changes, you'll go to the profile page where now you will see you're profile picture in a circular shape depending on the size, first and last names of the user above the username and the bio they put.
13. Below all of this is the ```posts``` and ```saved``` tabs. On the ```posts``` tab, there is where the posts the current user has posted can be seen. On the other hand the ```saved``` tab has the saved posts from other users. 
14. If a user wants to post something, they will click on the ```new post``` link on the navbar where they will choose the image, put a caption and tags. Once they post, their post will be in the posts tab and viewed by other users who follow the user who has posted.
15. Then there is the ```inbox``` link which will display the number of messages by the number and notify the user that they have received a message. On clicking it the number of messages will disappear and it will remain empty as before. If one clicks the inbox, they will see the message in the middle while on the left is some details of the sender of the messsage, like their profile picture, ```username```, ```first name``` and ```last name``` in a box that lights up blue meaning that is the most recent message. if one clicks on a previous one it also lights up as blue.
16. Below this sender details is a ```New message``` button which takes us to ```search users``` where one can search for other existing users by their username and if you find them, their profile picture, ```first name```, ```last name``` and ```username``` will be displayed. Then there is a ```send message``` button which if one clicks will automatically send a message saying ```Says Hello```. If there is no user it will display nothing. 
17. If the receiver of the message wants to reply to the meesage they have been sent they will simply fill in their message on the ```add comment``` section and their message will be displayed below the sender's message.
18. On the navbar there is the ```Notifications``` link which will light up just similarly like the ```inbox``` with the number of notifications. Then on clicking it, the number of notifications disappear. Then starting from the most recent notification to the latest they will be displayed. It will show the user who has liked you're post showing you their profile picture, the image they image they liked and how long ago they liked it. Then if a user follows you, one will see their names, profile picture and how long ago they followed you.
19. For a user to be able to follow another user, they need to go to the other user's profile where instead of seeing the ```edit profile``` they will se instead a ```follow``` button where if the click on it, the user will now be following the other user and the button changes to ```unfollow``` and vice versa.
20. Then there is the ```logout``` link which logs out a user.

## Known Bugs
* As a new user logs in, there are no images displayed as one has to follow a user to see their posts.
* Some profile picture images if are not proportional cannot fit in the rounded placeholder well.

## Contact Information

You can reach me on my email [royratchizi@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2021 **Roy Rasugu**