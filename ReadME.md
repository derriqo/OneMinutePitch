# ONE MINUTE PITCH


# Table of contents
***
* [General Info](#General-Info)
* [Technologies](#Technologies)
* [Setup](#Setup)
* [Behaviour Driven Technologies](#Behaviour-Driven-Technologies)
* [Support](#Support)
* [Bugs](#Bugs)
* [Creator](#Creator)
* [License](#License)

## General info
---
One minute pitch an application that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.

The application allows the user to:

* See the pitches other people have posted.

* Vote on the pitch they liked and give it a downvote or upvote.

* Be signed in for me to leave a comment

* Receive a welcoming email once I sign up.

* View the pitches I have created in my profile page.

* Comment on the different pitches and leave feedback.

* Submit a pitch in any category.

* View the different categories.

## Technologies
---
Project is created with:
* Python 3.6
* Prerequisites:   *Pip *SQLAlchemy
* Flask

## Setup
---
To run this project, please follow the following instructions.
-   Get access to the internet
-   Sign into your github pages. Set up would require access to github pages; the webpage uses an index file linked on github pages. This would require membership and access to the **derriqo** repository.
-   Search for derriqo on the github pages and select the One-Minute-Pitch repository.
-   Clone the repository.

### Cloning
---
* In your terminal:
        
        $ git clone https://github.com/derriqo/One-Minute-Pitch/
        $ cd One-Minute-Pitch

## Running the Application
---
* To run the application, in your terminal:

        $ chmod a+x start.sh
        $ ./start.sh
        
## Testing the Application
---
* To run the tests for the application file:

        $ python3.6 manage.py tes
        

## Behaviour Driven Development
---

**User Story**
As a user i want to be able to store my account credentials and their various passwords and also  be able to delete them.

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Welcomes user to the applicatin | **In terminal: $./run.py** | Hello, Welcome to Password Locker. What is your name? |
| Display codes for navigation | **In terminal: User enters Name** | Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential, ex -exit the credential list  |
| Display prompt for creating account | **Enter: cc** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: li** | Enter your account name and password |
| Display prompt for creating a credential | **Enter: cc** | Enter the site name, your username and password |
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Exit application | **Enter: ex** | Exit the current navigation stage |


## Support and contact details
---
For any inquiries, please reach out to derrick.william24@yahoo.com

## Bugs
---
None at the moment, but would love to hear your feedback!

## Creator
---

Created by Derrick William. 
