# Insta


## Description
- This is a basic django based Project. It is a clone of th famous instagram app. A user basically can do his usual activities that they do in instagram application. They can view posts from different users, Upload pictures of their choices from their local machines. A user can also comment on pictures and like differnt pictures.

## BDD
1. On load the User sees the User is prompted to register to the application.
   Input: The user enter their credentials as propted
   Output: The user is redirected to the log in page.
   NB: If the user enters wrong credentials he/she is prompted to enter new credentials. eg if the username is already taken.
2. The user is redirected to the log in page
   Input: The User enters the credentials that they used to sign up.
   Output: If the Information is entered correctly the user is redirected to the home page.
   NB: The User must enter correct information to proceed to the home page else they will be propted to re-enter their credentials.
3. The User can Update their Profiles
   Once A user is logged in their profile pages are loaded and User can Edit their Profiles.
   Input: A user types in the new profiles that they want.
   Output: After they are done success message appears that tells them that their info has been succesfully updated..
4. The user can upload an image
   When you hover over the navbar an icon that represents Uploading is seen.
   Input: The user uploads any image from their machines
   Output: The uploaded image is displayed on the home page.
## Setup and Installations
- clone the application `git clone <name of the repository>`
- Navigate into the folder whereby the application has been set up.
- Setup a virtual environment `virtualenv <environment name>` and activate it `source <environment_name>/bin/activate`
- Install the Requirements and Dependancies `pip install -r requirements.txt`
- Run the application `python3.6 manage.py runserver`
## Technologies Used
- dj-database-url==0.5.0
- Django==1.11
- django-bootstrap3==12.0.3
- django-heroku==0.3.1
- Pillow==7.0.0
- psycopg2==2.8.4
- python-decouple==3.3
- pytz==2019.3
- whitenoise==5.0.1
## Licence
The MIT License (MIT)
Copyright (c) 2020 Simon Kimani
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
## Contacts Information
- You can reach me at any time using : - +254702158483- kelvinmbuguaw@gmail.com
## Author
**Kelvin Mbugua**










