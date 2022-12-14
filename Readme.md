# student and course management system
### Made with love using Django Framework

## Installing and running the system
*Very first thing: Of course you should have a computer or laptop*😁

To begin with, make sure python is installed in your system.
You can install  Python ["Here"]("https://www.python.org/downloads/")
Check if python is install by typing `python --version` in the terminal
You should get something like this.
!['python version']('config\static\images\python.png')

✔All good?😊
>>Next
We need to install virtual environment.
To do this:
open terminal and run: `pip install virtualenv`
This may take some time.

After installing the virtual environment, we need to create a virtual environmet and activate it.

Navigate to the folder where the project `course_management_system` is located.
Your commandline should be something like this.
!['venv']('config\static\images\venv.png')

run, `python -m virtualenv venv`
then activate by running:
1. windows: `venv\scripts\activate`
2.Linux|Mac: `source env/bin/activate`

Now install requrements.
run: `pip install -r requirements.txt`

This will take a while depending on your internet speed.
When its done:
    --We are almost done--

Now run pyhton manage.py runserver to run the application.

The developement server will be running at port 8000 on the localhost.
Lets go ['there']('http://127.0.0.1:8000/') 🛫
Expectations:
!['home']('config\static\images\home.png')