Installation Instructions for Custom User
For Windows/Mac Users :
Install Python Ensure that you enable checkbox to install pip as well.

Open command prompt, change directory to the folder where you intend to save the project files.

Run python --version to check if Python was installed properly.

Run the following command to ensure you have pip installed in your system: $ pip --version

Clone project files from Github repository

Run https://github.com/CODEr-SaNjU/Custom_User.git Change Directory to folder Custom_User/ (where the pipfile exists)

Run pip install pipenv

Run pipenv shell to open the shell

Run pipenv install to install all the required packages for the project.

Change directory to Custom_User/Customsrc/ (where the manage.py file exists)

Run python manage.py makemigrations

Run python manage.py migrate

Run python manage.py runserver
