# Django Rest API (Todo Applicaion with Authentication)
A todo app with user authentication



### How to setup locally
#### Requirements

- Python
- pip
- virtualenv


#### setup instructions

- pull the project using git
```cmd
   git clone https://github.com/barkhayot/todo-api-drf.git
   ```
- create   a virtualenv using virtualenv
```cmd
   python -m pip install --upgrade pip
   pip install virtualenv
   virtualenv venv_name
   ```
- activate it 
```cmd
   source venv_name/bin/activate
   ```
- or activate Windows
```cmd
   venv_name/bin/activate.bat
   ```
- install dependencies from the requirements.txt file
```cmd
   pip install -r requirements.txt
   ```

- migrate the database tables
```cmd
   python manage.py migrate
   ```
- start a development server using 
```cmd
   python manage.py runserver
   ```
