# col_films

A platform that operates like a movie streaming platform but for short movies created by *college students*.

## Feature Requests
### User: Unauthenticated
- Visit the platform to view basic information about the platform
- View and Interact with the documentation
- Register to view more details
- No access to use until registered
- Able to view all available movies
### User: Authenticated

- Full access to the platform
- Allow upload of short movies (not more than 15 minutes)
- User must be a verified college student
- Watch films uploaded by others
- Comments, react and share movies
- Show usage example to users
- Allow user save data and come back to download

Project Documentation here @wiki  https://github.com/proj-team-111/col_films/wiki

# App Requirements
  -requirements.txt

# Architecture
  -Monolith(Django Templating)
  
# Installation Walkthrough
  1. Create a folder eg <code>Team_111</code>
  
  2. Change directory into the folder <code>cd Team_111</code>
  
  3. Clone main branch to the folder <code>git clone --branch main https://github.com/zuri-training/Col_Films_Team_111.git</code>
    now the path to the project is <code>Team_111/Col_Films_Team_111</code>
  
  4. Inside the project folder( <code>Col_Films_Team_111</code> ), create a virtual environment <code>python3 -m venv env</code> change directory into it     and activate it <code>source bin/activate</code> then exit the env <code>cd ..</code>
  
  5. Install the the dependencies <code>pip install -r requirements.txt</code>
  
  6. You can test the project by running <code>gunicorn col_films111.wsgi</code> you should see some lines of code that include <code>listening at: ...</code> . If you wish you can visit the address listed, it will take you to the landing page of the project.

  
  <strong>Note</strong>
  * As it is a django app, the allowed hosts have been set to <code>onecube.zurifordummies.com</code> if you need to make changes, it can be found in         <code>col_films111/settings.py</code>
  * It is important that the db.sqlite file is not tampered with and is present during deployment

