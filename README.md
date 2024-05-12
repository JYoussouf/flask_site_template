
Template Flask and Jinja site with a login, sign up, and placeholder notes application. Auth are credentials scrypt hashed.

## Set-up Instructions
- Set up a Python3.8 environment (not currently tested beyond that) 
`python3.8 -m venv env`
- Activate the environment and pip install requirements.txt flask packages
```
source env/bin/activate
pip install -r requirements.txt
```
- Create an `.envrc` file (I use [`direnv`](https://direnv.net/), but export your env variables as you'd like) and include the following environment variable:
```
export FLASK_APP=app
```
- In the home folder `flask_site_template/`, run `flask run`

## Views
_Template Log-in Page_
![image](https://github.com/JYoussouf/flask_site_template/assets/90774566/3eea26d1-592d-4be4-b0fa-2d404ee5fbaa)

_Sign up page with credential strength conditions and unique user validation_
![image](https://github.com/JYoussouf/flask_site_template/assets/90774566/7da419ba-7ccb-4c6a-832e-59bcd9d08bea)

_Placeholder notes application to test user writes to the database_
![image](https://github.com/JYoussouf/flask_site_template/assets/90774566/af9ade54-90f0-4e39-b748-2abf1f7b0261)
