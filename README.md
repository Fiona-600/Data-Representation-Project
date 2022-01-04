**Data Representation- 2021 Project Submission** <br/>
**GMIT Higher Diploma in Data Analytics** <br/>
**Submitted by Fiona Lee - 4 January 2022** <br/>

**Introduction**
***
This project explores the area of data representation by applying create, read, update, delete operations to databases using python and mySQL. 

Repository Link: https://github.com/Fiona-600/Data-Representation-Project.git
<br/>
<br/>
<br/>
![alt text](https://cdn.slidesharecdn.com/ss_thumbnails/datarepresentation-110727095418-phpapp01-thumbnail-4.jpg?cb=1311760556)
<br/>
<br/>

*Source: https://cdn.slidesharecdn.com/ss_thumbnails/datarepresentation-110727095418-phpapp01-thumbnail-4.jpg?cb=1311760556
<br/>
<br/>

**Purpose of the project**
***
The purpose of this project is to demonstrate an understanding of creating and consuming RESTful APIs.

The elements explored will be:

1. Create a web application in Flask that has a RESTful API.
2. Link the application to one or more database tables.
3. Create web page(s) that can consume the API. i.e. perform CRUD (Create, read, update, delete) operations on the data in the database.

<br/>

***The ClassTimetables Database***
***
<br/>

***About the Database***

The ClassTimetables database was created in mySQL to allow users to create, read, update, delete classes and bookings for a dog training school in real time via a web application.
<br/>
<br/>
***Tables***
<br/>
- Classes
- Bookings
<br/>
<br/>

**Attributes of the Tables**
<br/>
<br/>
The 'Classes' table contains the following information:
<br/>
- Class_ID: unique identifier with three components 1. the initials of the course, 2. the day of the week 'M','TU', 'W', 'TH','F and lastly the instance of that class on a given day.  An example classID would be 'AIM1' which represents the first agility improvers on Monday.
- Class_Name: 'beginners - obedience', 'improvers - obedience',  'agility - beginners', 'agility - improvers' and 'agility club'.
- Day: Day of week
- Time: Time of the class
- Max_Participants: Maximum number of places in the class
- Trainer: Trainer allocated to the class
<br/>
<br/>

The 'Booking' table contains the following information:
<br/>
- Dog_Name
- Class_ID: As above
- Class_Name: As above
- Day
- Time

It had been my intention to develop the booking table further however time dictated that I completed it to restserver stage and not fully to the web page stage.

<br/>

**Structure & Project Navigation**
***

The project will be stored in a GITHUB repository at url: https://github.com/Fiona-600/Data-Representation-Project.git
<br/>
<br/>

The GITHUB repository contains:

• A *'static pages'* folder which contains the file *'index.html'*. This file is the user interface and displays the output for the database.

• A *‘gitignore’* file containing any files or file types which should be ignored by the github repository.

• *'ClassesDAO.py'* and 'BookingDAO.py'* files which defines the access to and operations on the data in the data source i.e. the database (data access object).

• A *'configuration.py'* file which holds the login information to the database.

• A *'Create_tables'* file which sets up the initial database and tables.

• A *‘LICENSE’* file containing a copy of the MIT Licence

• A *'project-instructions.pdf'* file which outlines detailed instructions for the project 

• A *‘README.md’* file which contains:

  1.	The purpose of the project 
  2.  Information about the database and tables
  3.	Structure and project navigation
  4.	Required programs
  5.  Installing the requirements.txt file
  6.  Activating a virtual environment
  7.	Details of how to download and run the code 
  8.	Authors and contributors
  9.	References

• A *‘requirements.txt’* file containing information that facilitates the user to quickly run the notebooks with minimal configuration

• ‘rest_server.py’* files which sets up the live web user interface to the database using a Flask server application.

• *'test_ClassesDAO.py'* and *'test_ClassesDAO.py'* files which are test files for ClassesDAO.py and BookingDAO.py

<br/>

**Required Programs**
***
- Anaconda Navigator 3 - https://www.anaconda.com/
- Visual Studio Code - https://code.visualstudio.com/Download
- mySql communtiy server - https://dev.mysql.com/downloads/mysql/
- Python version 3.8.8 - downloaded via Anaconda Navigator 3 to Windows 10 operating system
- Cmder Console Emulator - https://cmder.net/
- GitHub Repository Storage - https://github.com/
- Firefox Internet Explorer - https://www.mozilla.org/en-US/firefox/new/

<br/>

**Installing the requirements.txt file**
***
- Type 'pip install -r requirements.txt' in the command line to install the file of python packages.
<br/>
<br/>

**Activating a virtual environment using the following commands on the command line:**
***
- *'python -m venv venv'* to create a blank virtual environment with a directory named venv.
- *'.\venv\Scripts\activate.bat'* in Windows or *'source venv/bin/activate'* in Mac/Linux.
- *'set FLASK_APP=application'* in Windows or *'export FLASK_APP=application'* in Mac/Linux to set the server environmental variable.  
- 'set FLASK_ENV=development'* in Windows or *'export FLASK_ENV=development'* in Mac/Linux to run in a development environment.
- *'flask run*' to run the server program and open the application on http://127.0.0.1:5000/. 
- Copy the link http://127.0.0.1:5000/ into your browser or hold *'Ctrl + click on link'* to open the web page.
- Hold *'Ctrl + c'* to stop the server running.

<br/>

**Downloading, opening and running the code**
***
  1.	Navigate to your desired location on your local drive using CMDER.
  2.  If you do not already have an SSH key, you will need to generate a new SSH key to use for authentication by typing the following into CMDER: ssh-keygen -t ecdsa-sk -C "your_email@example.com" (replace your e-mail address) and then save and choose a security passphrase.
  2.  Clone the github repository onto your local drive by using the command 'git clone git@github.com:Fiona-600/Data-Representation-Project.git' in CMDER.
  3.  Right click on the files in explore and 'open with visual studio code'
  4.
  5.	
<br/>


<br/>

**Author & Contributors**
***
**Author:** Fiona Lee

**Contributors:** I used the tutorials in Andrew Beatey's Github repository at https://github.com/andrewbeattycourseware/dataRepresenation2020 for reference

With thanks to Andrew for all the helpful tips in completing this project.

<br/>

**References**
***
[1] Andrew Beatty Github Repository: https://github.com/andrewbeattycourseware/dataRepresenation2020
[2] Flask Tutorial: https://www.tutorialspoint.com
[3] w3schools Tutorials:  https://www.w3schools.com/
[4] Moesif Origin & CORS Changer: https://chrome.google.com/webstore/detail/moesif-origin-cors-change/digfbfaphojjndkpccljibejjbppifbc