# Programming Test

My solution was made using python and sqlite.  Task 1 said to find the people who have visited the most sites, 
but it didn't specify whether to count all sites visited by a person or only include distinct sites.  So, I made two programs.  `programmer_test.py` counts **all sites** visited by a person, while `programmer_test_distinct.py` counts **all distinct sites** visited by a person.

Before running the program make sure you have python installed and that the python paths are correctly configured.  To run `programmer_test.py`, simply download it along with the testdb.db file.  Place both files in the same folder and navigate to that folder from the command line.  Then, from within the directory, run the following command:
```
python programmer_test.py
```
You should see the results printed out in the command line.  The same can be done for `programmer_test_distinct.py`.

That should cover tasks 1-4.  

# Extras- Docker and API
The "Extras" folder contains files to implement the `programmer_test_distinct.py` program with an API deployed using docker and Flask. Download the `test app` folder and navigate to it through the command line.  To set up your instance, run the following commands: 
```
docker-machine create -d virtualbox test-app-vm
docker-compose build
docker-compose up -d
```
The first command creates a virtual machine.  The next two commands build and then set up your app.  Once it's deployed you can try it out by sending a request from the command line using curl.   For example:
```
curl http://192.168.99.100/result
```
However, make sure you change the address to the corresponding one for your virtual machine.
