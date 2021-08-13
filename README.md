# ChatterBox, a Flask Based Web Application.

Utilizing Python with Flask, JavaScript, JSON, HTML/CSS, and SQLAlchemy.

## Getting Started:
* Clone the repository, and navigate to the `chatterbox-web-chat` folder
* Make sure Flask is installed and you have initialized the environment - details on how to do so can be found at: https://flask.palletsprojects.com/en/2.0.x/installation/
* Set the `FLASK_APP` environment variable to `chat.py` (set FLASK_APP=chat.py)
* Initialize the database by running `flask initdb` 
* Run the app with `flask run`

## Next Steps:
* Once running, the newly initialized database will not contain any user accounts or messages yet.
* Follow the website navigation to create a new user.
* Log-in with the new user, and begin creating chat rooms.
* You can navigate between chatrooms and send messages in any that exist.
* You can create as many users/chat rooms as you want! Users only have permission to delete the chat rooms that they have personally created.
