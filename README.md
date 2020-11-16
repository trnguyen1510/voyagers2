

![Voyagers](https://i.imgur.com/bFX5bJs.png)

# Voyagers
### Never Travel alone!
![Voyagers](https://media.giphy.com/media/FxTcyJKmxWys88EWHD/giphy.gif)

Voyagers provides a platform that helps people match their travel companions based on their customized travel profiles and preferences.

Voyagers provides holiday package tours to famous destinations and attractions, as well as popular local activities.

Voyagers will offer inexperienced and experienced travelers who are seeking travel companions to go abroad and share their experiences with their new group of friends.

![](https://media.giphy.com/media/IaATK5t6s5vvWT4Bc6/giphy.gif) **Background Story**

Planning an entire days-long trip can be quite hectic. Not only do travelers have to plan out the accommodations, attractions, and transportation, they may also have to recruit their own travel buddies themselves and there is a huge chance that their friends won’t be able to travel with them. These tasks can be time-consuming and redundant. It can also be quite intimidating because of the lack of understanding, especially for inexperienced travelers. A good full-package travel planning service can be very helpful in this case. While many current travel service platforms focus on providing travel packages and deals to a group of travelers, few assess the social importance of tour groups amongst the travelers. Fewer give the options for the attendees to get to know their companion travelers beforehand if they meet through the tour package. At Voyagers, we work hard to provide full holiday packages with modern themed experiences, and matching service for like-minded travelers to group up for their next adventure.
## Application Requirements
 1. Python 3.8.5 or newer
 2. Django 3.1.2
 3. Pip
 4. Virtual Environment
 5. pytest
 6. Other packages listed in requiremtns.txt
## How to install and run Voyagers App
Make sure you have already downloaded and install python3 and pip
#### Initial setup and run the website
1. The first thing to do is to clone the repository:
 ```sh
$ git clone https://github.com/jygjyg123/Voyagers.git
$ cd Voyagers
`````````````

2. Create a virtual environment to install dependencies:
- For MacOS: 
 ```sh
$ python3 -m venv env 
`````````````

- For Windows:
 ```sh
C:\Users\Name\Voyagers> py -m venv env
`````````````
3. Activate your Virtual Environment
- For MacOS:
 ```sh
$ source env/bin/activate
`````````````
- For Windows:
 ```sh
C:\Users\Name\Voyagers> env\Scripts\activate 
`````````````
4. Install dependencies listed in the requirement.txt:
 ```sh
(env)$ pip install -r requirements.txt 
`````````````
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `py -m venv env`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd voyagers
```
5. Run Server
```sh
(env)$ python manage.py runserver
```
Expecting result: 
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 03, 2020 - 00:26:12
Django version 3.1.2, using settings 'voyagers.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

6. If you cannot run step 5, You may have to migrate any unapplied migrations by : 
```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```
After this run Step 5 again. 

And navigate to Voyagers homepage using `http://127.0.0.1:8000`.

#### Other syntaxes
To kill/stop the server 
> Ctrl + c

To deactivate the Virtual Environment
```sh
(env)$ deactivate
```
## Tests
 **Instruction**
 Make sure your Virtual Environment is activated. 
To run pytest `cd` into the directory where `manage.py` is and run: 
```sh
(env)$ pytest
``` 
**Expected Result**

![pytest_screenshot](https://i.imgur.com/nksfbiK.jpg)

## How to use the website
- Users have access to `Sign up` , `Log in`,`About us`, `Upcoming Tours` and `Contact` pages from top menu bar. 
- Create user account from `Sign Up` page, or if users already have an account with us, simply sign in using `Log In` page. 
- After `Log In` users can also have access to their `Profile Dashboard` and be able to edit the information through the `Setting` tab locating at the end of the side menu. 
- If users want to learn more about our website's concept click `About us`
- We also have a contact form that is attached to the bottom of our About Us page, or users can simply click `Contact` in the menu bar.
- `Upcoming Tours` displays all of our available and incoming tours if users haven't answered our `Tour Preferences` questions (Milestone 2) or if users only want to check out what do we offer for the next six months. 
- In `Upcoming Tours`, we offer a search bar that help users to filter out the city they would like to see. The `All` button would help to redisplay all availabled tour packages. 

## Application Concept

### Targeted Demographics

College students, newly graduates, young professionals, unexperienced or experienced travelers.

### Main Features

* Package Tours and add-on options

* Matching Travelers based on preferences 

* Tour packages with famous destinations and activities

### User Stories

## User Stories

 - As a user, I want to be able to sign up for the travel webite.
 - As a user, I want to be able to log in for the travel website.
 -   As a user, I want to ensure my sign up credentials fulfill the
   website's requirement. 
- As a user, I want to read the feedbacks from previous users.
- As a user, I want to see the list of upcoming tours and their prices.
- As a user, I want to be able to search for tours by destination name
   (city).
 - As a user, I want to know more about the travel website and their
   background.  
- As a user, I want to view the travel website's contact information.  
- As a user, I want to see previous trips photos.
- As a user, I want to see the travel website's partners.
- As a user, I want to have a user dashboard contains my information,
   resume so that other users can take a look.  
- As a user, I want to be able to edit my profile and personal information.
### Stakeholders
- End users and Beneficiaries
- Direct users
- Beneficiaries: airline companies, local tour vendors, airBnB, local hostels, etc.
- Project build team 
 - Developers
 - Project Managers
 - Legal Department (for advice about data protection regulations, identities scanning)
- Sales and Customer Services team
# Milestone 1.0

## Iteration 1 
> 15 calendar days, 11 working days (60% velocity)
> Days of actual work: 5 * 15 * 0.60 = 45 days


![BurnoutIteration1](https://i.imgur.com/NH4dHZJ.jpg)

### Work breakdown

:white_check_mark: Welcome Page - Kennenth and Tracy 
(including feedbacks)

> Priority : 10
> EST. 6 days

:white_check_mark: About Us - Kennenth and Tracy 
(including contact information)

> Priority: 20

> EST. 6 days

:white_check_mark: Sign In Page (Front End) - Kenneth and Tracy
> Priority: 10
> EST. 8 days

:white_check_mark: Sign Up Page (Front End) - Kenneth and Tracy 
> Priority: 10
> EST. 9 days

:white_check_mark:  Sign In (connect and perform authentication) - Tayo/Jerry/Karthik 

> Priority: 10
> EST. 8 days 

:white_check_mark:  Sign Up (connect and store in database) - Tayo/Jerry/Karthik

> Priority: 10
> EST. 8 days

## Iteration 2
> 12 calendar days, 9 working days (60% Velocity)
> Days of actual work: 5 * 12 * 0.60 = 36 days 


![Iteration2Burnout](https://i.imgur.com/bHv78Sn.jpg)

### Work breakdown 

:white_check_mark:  User Profile (front end) Tracy/Ken/Tayo
> Priority: 30
> EST.  9 days

:white_check_mark: Editing Page (front end) - Tracy/Tayo/Karthik
> Priority: 20
> EST.  9 days

:white_check_mark:  Tour packages display page - Jerry/Tracy 
(including tour names, prices, EST. departure dates)
> Priority: 20
> EST.  9 days 

:white_check_mark:  Search bar for tours - Tracy/Jerry
> Priority: 30
> EST.  9 days 

### Velocity 

* Total Day: 27 calendar days (until 11/03/2020 Milestone 1 is due)
* Working Day: 20 days 
* Velocity. = ~60% (subject to change. Range from 60% - 75%) 

**Team's Trello link:** https://trello.com/b/gdYNZyem



## Team 

![Voyagers](https://media.giphy.com/media/ecxPmlUNAJFzGFXg6X/giphy.gif)

 - Tracy Nguyen

 - Kenneth Carmona

 - Tayo Arikenbi

 - Jerry Jiang

 - Karthik Purna
# Milestone 2.0

1. Tour preferences quiz
2. Matching companions based on tour preferences 
3. Tours detail and booked users display 
4. Other users can review the booked-users' dashboards



