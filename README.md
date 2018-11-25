# Logs Analysis Project

This is my version of the Logs Analysis project, which is an internal reporting tool that uses information from a news database, to discover what kind of articles the site's readers like. Provided the following questions I wrote a python script(main.py) to answer them using SQL queries:
 1. What are the most popular three articles of all time?
 2. Who are the most popular article authors of all time?
 3. On which days did more than 1% of requests lead to errors?

## Run the program

 1. You need to have installed:
    - A version of Python (at least 2.7 and above).
    - The [Vagrant](https://www.vagrantup.com/) tool for building and managing virtual machine environments.
    - Linux on the [VirtualBox](https://www.virtualbox.org/) Virtual Machine.
 2. Launch the Virtual Machine by:
    - Launch the Vagrant Virtual Machine inside your shared Vagrant sub-directory by running: `$ vagrant up`
    - Then ssh using this command: `$ vagrant ssh`.
 3. Download and place the project files into a folder in your shared Vagrant sub-directory and navigate to that folder. You'll also need to do that with the database [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). The file inside is called newsdata.sql.
 4. Load the data from __newsdata.sql__ into your local database by running: `$ psql -d news -f newsdata.sql`.
 5. Use the PostgreSQL command line program to connect to the database named news which has been set up for you by running: `$ psql -d news`.
 6. Run the Python script from your vagrant sub-directory using Python: `$ python main.py`.

## Dependencies

- The main.py script relies on the psycopg2 wrapper around libpq, to expose a Python DB-API compatible API to the program.
- The script also relies on the datetime module, which supplies classes for manipulating the date of the 3rd query.