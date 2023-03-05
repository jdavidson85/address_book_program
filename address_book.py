file = open("text.file", "w")
number = int(input("How many people do you want to add to this file?"))
for i in range(number):
    name = input("What is the name of person?")
    phone = input("What is their phone number?")
    email = input("What is their email?")
    file.write(",".join([name, phone, email]) + '\n')
file.close()
