My program was made using python and sqlite.  Task 1 said to find the people who have visited the most sites, 
but it didn't specify whether to count all sites or only include distinct sites.  So, I made two programs:  

programmer_test.py counts all sites visited by a person
programmer_test_distinct.py counts all distinct sites visited by a person.

To run programmer_test.py, simply download it along with the testdb.db file.  Place both files in the same folder and navigate to that folder from the command line.  Then, from within the directory, run the command python programmer_test.py and you should see the results printed out in the command line.  The same can be done for programmer_test_distinct.py.

That should cover tasks 1-4.  The Extras folder contains files to implement the programmer_test.py program with an API deployed using docker and Flask. Download the test app folder, navigate to it through the command line.

To set up a virtual machine, run the command docker-machine create -d virtualbox housing-app-vm
Then run the following commands:
docker-compose build
docker-compose up -d

Once it's deployed you can try it out by sending a request from the command line using curl.  Example:
curl http://192.168.99.100/result
