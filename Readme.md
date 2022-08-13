## **Python Behave BDD Framework**

This is a BDD automation framework developed on Selenium and Python Behave.
Sample test side used in this project is - https://beta.speedhome.com/

Page Object Model is followed in this framework

**pages** folder contains the elements and corresponding actions of the pages

**features** folder contains **steps** folder which has all the test files and also the feature files.


**requirements.txt** file contains all the python packages needed to run this framework

**allure** directory contains the files generated with allure reports

### **Commands to run the tests**

**To run the test with allure report**
` behave -f allure_behave.formatter:AllureFormatter -o allure/results ./features`
' behave -f allure_behave.formatter:AllureFormatter -o allure/results ./features -D'

**To run the test without allure report** 
`behave features`


To run this test. Following steps are mandatory.
Download Pycharm with Python 3.9 Interpreter
Selenium 4.1 (Go to terminal at the bottom and type in command pip install ./ requirements.txt)

requirements.txt file contains all the packages needed to run these tests.

To run all the test and generate report on behave you can use the following command
** behave features **
"Will run all the tests sequentially"

To run individual feature file.
** behave "file_name".features 



or you can directly run individual tests or individual file from the file itself by click on Play button.