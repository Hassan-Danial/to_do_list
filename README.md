# TO DO List

## Overview

TO Do app is a simple CRUD (create, read, update and delete) task scheduling app which helps us in keeping tracks of our tasks with due date of that task.
## Key Topics

* How to install the repo
* List of features that the code performs
* Example to run the code features
* How to run test cases

## Installling Repository

Follow following steps to install repository on your local system
1. Before install requirements, you should install Virtual Environment tools for python project, if you have installed then activite the virtual enivronment in your project, otherwise run this command to install virtual environment in your project **Python3 -m venv {project_name}**
2. The names of dependencies for this repository are stored in **requirements.txt** along with versions. You can install all the dependencies using one command **pip install -r requirements.txt** in you virtual environment.
3. To check the tools installed in your virtual environment, you can run command like **"pip list"**
4. I fyou have contributed in project and installed new dependencies as you requirements then to save new dependencies in **requirements.txt** file use command **"pip freeze > requirements.txt"** 
5. You should not push changes to repository along with requirement.txt which hold your dependencies. If you notice the virtual Environment file name is included in **.gitignore** file so that virtual environment does not pushed on to remote repository along with other changes. Anyone who need repo can install those dependencies with one single command.

## List of features that the code performs

- **Create** or Add a task in your tasks list, just click on **Add Task** button on top right corner of home page and you can easily add tasks.
- To only **read** the content of the tasks, just click on the task and the title, due date and description of task will be visible.
- To **update** a task, just click on update button next to a task, a form will open containg already setted due date, title and description, you can make any changes and clickon submit button.
- In any view there is a **Abort** or **Back** button in case you do not want to make changes.
- To **delete** a task just click on delete and app will ask for permision to delete, click submit and it will be deleted.
- Once a task is marked completed, app will **cut the text of task title**, indicating that task is completed.
- **Search bar** is given to search through all tasks.
- A header bar is given indicating the remaining tasks to complete.