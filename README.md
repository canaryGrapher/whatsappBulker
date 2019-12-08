# whatsappBulker
This tool makes it easy to send bulk messages to a lot of people on WhatsApp without the need to save all the numbers on your smartphone

## How to use this tool?
Using  this tool is pretty easy. There are few requirement you are required to meet before you can use this too.

1. You need to have Python installed on your device
2. You need to be logged into the Web WhatsApp portal

## Guide for Windows users
1. If python is not already installed, you can get it from [here](https://www.python.org/downloads/release/python-2716/). 
2. Now, given that you given that you already have the data set of the numbers, save those in the **rawNumber.txt** file. Make sure that you enter each number in a new line. If you are adding those number, make sure that all of them either have the country code pre-fixed, or they don't. Don't mix it with each other. 
3. Now fire up your Command Prompt and navigate to the folder where this file is saved. After navigating there, run the **whatsappAPI.py** script. Also, make sure that no web.whatsapp.com tab is open.
```python whatsappAPI.py```
4. Now, run another python script named **automateMessage.py** using the command ```python automateMessage.py```. Your default web browser will automatically open a new [WhatsApp](https://web.whatsapp.com) tab. Proceed with the steps and when the message is sent, close the tab.
5. Press **_Enter_** twice on the keyboard in the command prompt window. This will have open another tab in the Browser. You'll have to do this step after every message is sent. 

## Guide for Linux users
1. If python is not already installed, you can install it by using the ```sudo apt-get install python``` command in the terminal. Enter your password and let it install.
2. Now, given that you already have the data set of the numbers, save those in the **rawNumber.txt** file. Make sure that you enter each number in a new line. If you are adding those number, make sure that all of them either have the country code pre-fixed, or they don't. Don't mix it with each other. 
3. Now fire up your terminal and navigate to the folder where this file is saved. After navigating there, run the **whatsappAPI.py** script. Also, make sure that no web.whatsapp.com tab is open.
```python whatsappAPI.py```
4. Now, run another python script named **automateMessage.py** using the command ```python automateMessage.py```. Your default web browser will automatically open a new [WhatsApp](https://web.whatsapp.com) tab. Proceed with the steps and when the message is sent, close the tab.
5. Press **_Enter_** twice on the keyboard in the terminal window. This will have open another tab in the Browser. You'll have to do this step after every message is sent. 

## Guide for Mac users
1. If you have a Mac OS X 10.8 or higher, python is installed on your device by default. You need not install it again. However you are free to upgrade it to a more recent version.
2. Now, given that you already have the data set of the numbers, save those in the **rawNumber.txt** file. Make sure that you enter each number in a new line. If you are adding those number, make sure that all of them either have the country code pre-fixed, or they don't. Don't mix it with each other. 
3. Now fire up your terminal and navigate to the folder where this file is saved. After navigating there, run the **whatsappAPI.py** script. Also, make sure that no web.whatsapp.com tab is open.
```python whatsappAPI.py```
4. Now, run another python script named **automateMessage.py** using the command ```python automateMessage.py```. Your default web browser will automatically open a new [WhatsApp](https://web.whatsapp.com) tab. Proceed with the steps and when the message is sent, close the tab.
5. Press **_Enter_** twice on the keyboard in the terminal window. This will have open another tab in the Browser. You'll have to do this step after every message is sent. 


### Note for developers
If you have experience with selenium, try automating the process of clicking the buttons automated so the there is close to zero human input in this process. Your contribution will be appreciated and recognized. Thanks :)
