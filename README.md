# Pitches
## Author
Rowena Rono

# Description
This  is a flask application that allows users to post one minute pitches and also allows other users who have signed up to comment and upvote or downvote a pitch. It also allows a person to signup to be able to access the functionalities of the application

## User Story

* Comment on the different pitches posted py other uses.
* See the pitches posted by other uses.
* Register to be allowed to log in to the application
* View pitches from the different categories.
* Submit a pitch to a specific category of their choice.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all posts, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with app pitches based on categories and commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|

## Development Installation
To get the code..

## Live Link
* <pitches34.herokuapp.com/>
1. Cloning the repository:
  ```bash
  https://github.com/glasses-png/pitch.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd pitches
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3.6 manage.py server
  ```
5. Testing the application
  ```bash
  python3.6 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.

## Bugs
No known bugs.


## Technology used

* Python3.6
* Flask
* Heroku


## Contact Information

If you have any question or contributions, please email me at rowenarono@gmail.com

### License

* [[License: MIT]](Licence.md) <rowenarono@gmail.com>
