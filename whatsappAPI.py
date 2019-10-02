with open("rawNumber.txt", "r") as g:
    numberPerson = g.readline()
    with open("file.txt", "w") as q:
        for line in g:
            numberOfPerson = line[:-1]
            header = "https://api.whatsapp.com/send?phone="
            number = "91"+numberOfPerson
            message = "&text=Hello! This is a reminder message for an internship that you applied for, at the Innovation Center, MIT as a web developer/designer and with other proficient skills. Please be ready at 6:30pm tomorrow, i.e., Saturday at Co-working space, First Floor, IC."
            q.write(header)
            q.write(number)
            q.write(message)
            q.write("\n")
            q.write("\n")
    q.close()
g.close()
