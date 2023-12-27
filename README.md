# dreamTask
TCP server testing

# Project Title

this project testsing TCP server <br>
the docker running a TCP server listening on a predefined port (9001). <br>
the code connects to the server and listens for incoming TCP connections. <br>
For every connection it accepts, the server reads the first byte sent (and only the first byte). <br>
All test results are displayed in allure deshboard  <br>

## Installation

install docker and load the image <br>
install pytest <br>
install allur-pytest <br>

## Step By Step

start the server (with docker) <br>
run the tests in terminal with : pytest --alluredir=./allure-results test_microservice.py<br>
to see the results on the deshbord : allure serve ./allure-results  <br>
