import webbrowser

with open("file.txt", "r") as f:
    for line in f:
        print(line)
        webbrowser.open(line)
        waitConfirm = input("Enter confirmation command")
        if waitConfirm == '\n':
            continue
