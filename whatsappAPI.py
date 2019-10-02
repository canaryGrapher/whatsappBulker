with open("rawNumber.txt", "r") as g:
    numberPerson = g.readline()
    with open("file.txt", "w") as q:
        for line in g:
            numberOfPerson = line[:-1]
            header = "https://api.whatsapp.com/send?phone="
            number = "91"+numberOfPerson
            message = "&text=your_message_here."
            q.write(header)
            q.write(number)
            q.write(message)
            q.write("\n")
            q.write("\n")
    q.close()
g.close()
