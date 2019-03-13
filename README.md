Quiz Stats
----------

This is a short app that will quiz a user, and display stats on all user's results.


Database Setup:
----------
```
sudo su - postgres
psql
CREATE DATABASE <desired_database_name>;
CREATE USER <desired_username> WITH PASSWORD '<desired_password>';
\q
exit
```


Python Dependencies Setup:
----------
From root directory:
```
source venv/bin/activate
pip install requirements.txt
```
Copy provided `settings.py` file to `quiz_stats/quiz_stats/settings.py`. If you wish to change database credentials, they are on lines 83, 84, and 85.


Django App Superuser Setup:
----------
From root directory:
```
source venv/bin/activate
python manage.py createsuperuser --username=admin --email=anything@example.com
```
Password entered at prompt must be at least 8 characters.


To Run App:
----------
Complete database, Python dependencies, and Django app superuser steps.
From root directory:
```
source venv/bin/activate
python quiz_stats/manage.py runserver
```

App will start at 127.0.0.1:8000. The front end is at `/index/`, the admin dashboard at `/admin/`, and all API endpoints begin with `/api/`.


API Endpoints:
----------
GET
`/api/project`
-- returns all projects

GET
`/api/project/<project_id>`
-- returns specific project

POST
`/api/project`
-- create new project

POST
`/api/project/<project_id>`
-- edit existing project

GET
`/api/token`
-- returns all tokens

GET
`/api/token/<token_id>`
-- returns specific token

POST
`/api/token`
-- create new token

POST
`/api/token/<token_id>`
-- edit existing token

GET
`/api/question`
-- returns all questions

GET
`/api/question/<question_id>`
-- returns specific question

POST
`/api/question`
-- create new question

POST
`/api/question/<question_id>`
-- edit existing question

GET
`/api/relationship`
-- returns all relationships

GET
`/api/relationship/<relationship_id>`
-- returns specific relationship

POST
`/api/relationship`
-- create new relationship

POST
`/api/relationship/<relationship_id>`
-- edit existing relationship

GET
`/api/answer`
-- returns all answers

GET
`/api/answer/<answer_id>`
-- returns specific answer

POST
`/api/answer`
-- create new answer

POST
`/api/answer/<answer_id>`
-- edit existing answer
