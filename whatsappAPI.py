import webbrowser
import time
import os

countryCode = input("Country code for this batch: ")
with open("rawNumber.txt", "r") as g:
    numberPerson = g.readline()
    with open("file.txt", "w") as q:
        for line in g:
            numberOfPerson = line[:-1]
            header = "https://api.whatsapp.com/send?phone="
            number = "+" + str(countryCode) + numberOfPerson
            addMessage = "&text="
            message = "your_message_here."
            q.write(header)
            q.write(number)
            q.write(addMessage)
            q.write(message)
            q.write("\n")
    q.close()
g.close()

with open("file.txt", "r") as f:
    for line in f:
        print(line)
        webbrowser.open(line)
        print("Enter confirmation command")
        os.system("pause")
