# whatsappBulker
This tool makes it easy to send bulk messages to a lot of people on WhatsApp without the need to save all the numbers on your smartphone

## How to use this tool?
Using  this tool is pretty easy. There are few requirement you are required to meet before you can use this too.

1. You need to have Python installed on your device
2. You need to be logged into the Web WhatsApp portal

## Guide for Windows users
1. If python is not already installed, you can get it from [here](https://www.python.org/downloads/release/python-2716/). 
2. Now, given that you have the given data set of the numbers, save those in the **rawNumber.txt** file. Make sure that you enter each number in a new line. If you are adding those number, make sure that all of them either have the country code pre-fixed, or they don't. Don't mix it with each other. 
3. Now fire up your Command Prompt and navigate to the folder where this file is saved. After navigating there, run the **whatsappAPI.py** script. ```python whatsappAPI.py``` Now, another python script **automateMessage.py** will automatically execute. Your default web browser will automatically open a new [WhatsApp](https://web.whatsapp.com) tab. Proceed with the steps and when the message is sent, you'll automatically 
