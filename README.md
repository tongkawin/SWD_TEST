# Python Developer Test (Swift Dynamic)
## Installation
```
git clone https://github.com/tongkawin/SWD_TEST.git
```
## 1.1 Numbers to Thai Words
#### Run code
```
python 1.1.py
```
## 1.2 Numbers to Roman
#### Run code
```
python 1.2.py
```
## Special score: Numbers to Thai Words
#### Run code
```
python special_score.py
```
## 2.1 Todo app
#### Run project
```
python manage.py runserver
```
#### API List
Create task: http://localhost:8000/api/task-create/
Task List: http://localhost:8000/api/todo-list/
Task Detail: http://localhost:8000/api/task-detail/{id}
Update task: http://localhost:8000/api/task-updates/{id}
Delete task: http://localhost:8000/api/task-delete/{id}
#### Create task (http://localhost:8000/api/task-create/)
Input content as below.
```
{
    "title": "Task title",
    "Completed": true or false
}
```
#### Task List (http://localhost:8000/api/todo-list/)
Show all the tasks that you create.
#### Task Detail (http://localhost:8000/api/task-detail/{id})
Show more detail by task ID.

#### Update task (http://localhost:8000/api/task-updates/{id})
Update task by task ID.
Input content as below.
```
{
    "title": "Task title",
    "Completed": true or false
}
```
#### Delete task (http://localhost:8000/api/task-delete/{id})
Delete task by task ID.
## 2.2 Send email
You have to access your SMTP first.
#### Config
Config in ./EmailSender/settings.py
```
EMAIL_HOST_USER = 'YOUR EMAIL'
EMAIL_HOST_PASSWORD = 'YOUR EMAIL PASSOWRD'
```
Config in ./send/views.py
```
['TO EMAIL']
```
#### Run project
```
python manage.py runserver
```
## 2.3 Find array index of highest value
```
python 2.3.py
```
## 2.4 Find amount of 0
```
python 2.4.py
```
> Note: This is my first time with django python.
