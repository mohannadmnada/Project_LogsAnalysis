- Log Analysis Project 
Source code for a Log Analysis Project.


By ’Mohannad Mahmoud Nada.


- Resources
Udacity
Stackoverflow


This is the 3rd project made for the  fulfillment of [Udacity's Full Stack Web Development Nanodegree]

- The project's main focus was to put the sql and queries at test after the basic indtroduction to sql in the nanodegree lessons.
- The main target was to analyze log entries of a database.



- Files
 
"Project3.py" is the file where the queries are defined, executed and saved into a txt file.

"Output.txt" is the file where the questions of the project and the query results for these questions are saved.



-Make sure you have `newsdata.sql`, the SQL script file with all the data. It can be downloaded from the Udacity course page 

Technologies used
PostgreSQL
Writing Python code with DB-API
Linux-based virtual machine (VM) Vagrant
Project Requirements
Reporting tool should answer the following questions:

What are the most popular three articles of all time?
Who are the most popular article authors of all time?
On which days did more than 1% of requests lead to errors?
Project follows good SQL coding practices: Each question should be answered with a single database query.
The code is error free and conforms to the PEP8 style recommendations.
The code presents its output in clearly formatted plain text.
System setup and how to view this project
This project makes use of Udacity's Linux-based virtual machine (VM) configuration which includes all of the necessary software to run the application.

Download Vagrant and install.
Download Virtual Box and install.
Download the newsdata.sql
Run these commands from the terminal in the folder where your vagrant is installed in:
vagrant up to start up the VM.
vagrant ssh to log into the VM.
cd /vagrant to change to your vagrant directory.
psql -d news -f newsdata.sql to load the data and create the tables.
python3 newsdata.py to run the reporting tool.