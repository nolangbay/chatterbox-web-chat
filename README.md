# ChatterBox, a Flask Based Web Application.

Written in Python, JavaScript, and HTML/CSS, utilizing SQLAlchemy.

## Getting Started:
* Clone the repository, and navigate to the `chatterbox-web-chat` folder
* Make sure Flask is installed and you have initialized the environment - details on how to do this can be found here: https://flask.palletsprojects.com/en/2.0.x/installation/
* Set the `FLASK_APP` environment variable to `chat.py` (set FLASK_APP=chat.py)
* Initialize the database by running `flask initdb` 
* Run the app with `flask run`

## Next Steps:
* Once running, the newly initialized database will not contain any user accounts or messages yet.
* Follow the website navigation to create a new user.
* Log-in with the new user, and begin creating chat rooms.
* You can navigate between chatrooms and send messages in any that exist - chat messages are polled live.
* To test multiple users at the same time, set up multiple Chrome profiles: https://support.google.com/chrome/answer/2364824?hl=en&co=GENIE.Platform%3DDesktop
* You can create as many new users and chat rooms as you want! Users only have permission to delete the chat rooms that they have personally created.

<br>
<img src="https://user-images.githubusercontent.com/54992835/129320119-0623b8a0-7269-4fee-8ce0-75ec4b28426c.gif" width="500">
