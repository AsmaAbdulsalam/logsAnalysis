# Project Title
Internal Reporting Tool- Udacity - first project.
This project is for creating a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
What things you need to install the software and how to install them
-In this project You'll be using a Unix-style terminal on your computer. 
If you are using a Mac or Linux system, your regular terminal program will do just fine. 
On Windows, we recommend using the **Git Bash** terminal that comes with the Git software. 
If you don't already have Git installed, download Git from https://git-scm.com/downloads

-You'll use a virtual machine (VM) to run an SQL database server and a web app that uses it. 
The VM is a Linux server system that runs on top of your own computer.
You can share files easily between your computer and the VM;  
-We're using tools called **Vagrant** and **VirtualBox** to install and manage the VM. 
If you don't already have them you can download them
Vagrant: from https://www.vagrantup.com/
VirtualBox: from https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
-Python program.


### Installing
-If you don't have python on your computer you can Installs python form ...
We're using tools called Vagrant and VirtualBox to install and manage the VM.
You do not need to launch VirtualBox after installing it; Vagrant will do that. 
-Download vagrant from https://www.vagrantup.com/
-Download VirtualBox from https://www.virtualbox.org/wiki/Download_Old_Builds_5_1

Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the current release of Vagrant.
Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.
To make sure if Vagrant is successfully installed, try to run on in the terminal **"vagrant --version"** to see the version number.

-You can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.
	you will end up with a new directory containing the VM files. Change to this directory in your terminal with **cd**. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:
-To start up the virtual machine:
	From your terminal, inside the vagrant subdirectory, run the command **"vagrant up"**.
	When vagrant up is finished running, you will get your shell prompt back.
	At this point, you can run **"vagrant ssh"** to log in to your newly installed Linux VM!
	Inside the VM, change directory to /vagrant by typing **"cd /vagrant"**.
-To run the database:
	If you need to bring the virtual machine back online (with vagrant up), do so now. Then log into it with "vagrant ssh".
	After logging into the VM using "vagrant ssh" from your terminal, then type "cd /vagrant"
	To build the reporting tool, you'll need to load the site's data into your local database by typing "psql -d news -f newsdata.sql". This won't work until you download the database and unzip it and move it to vagrant directory.
	Once you have the data loaded into your database You don't need to re-load the site's data every time, you can run **"psql news"** only.

## Running the tests
Make sure you ave downland all the required programs.
Open the git bash in vagrant file: open "FSND-Virtual-Machine" file >> "Vagrant" file click right on "Git bash hare". Terminal window will be opened.
Type **Vagrant up** an wait for few minutes. When vagrant up is finished running, you will get your shell prompt back.
Then type **Vagrant ssh** to log in.
Go to Vagrant Directory by typing **CD /vagrant** , **ls** to explore the directory.
Go to project1 Directory by typing **CD project1**, **ls** to explore the directory. Make sure you have (newsdata.sql  p1.py  readme.txt)
-To run the reports and see the output:
	run "**python p1.py**".
-To load the data type** psql -d news -f newsdata.sql, but if you have already run this before you can run **psql news**.

### Break down into end to end tests
This project makes three queries.
The first one Returns the most popular three articles from the 'database', most popular article at the top.
The second one Returns the most popular article authors from the 'database', most popular author at the top.
And The last one Returns the days that lead to errors more than 1%.
The output will look like this:
	The most popular three articles:
	"Candidate is jerk, alleges rival" _ 338647 views
	"Bears love berries, alleges bear" _ 253801 views
	"Bad things gone, say good people" _ 170098 views


	The most popular article authors:
	Anonymous Contributor _ 170098 views
	Markoff Chaney _ 84557 views
	Rudolf von Treppenwitz _ 423457 views
	Ursula La Multa _ 507594 views


	the days that lead to errors more than 1%:
	2016-07-17 _ 2.26% errors

	
### And coding style tests
The code consists of three methods each method execute one query and print it.

## Authors
***Asma Abdullah Abdulsalam** - *Student in KAU and Udacity*

## Acknowledgments
* many thanks to our section leader Miss. Mashael 
