def main():
    number = int(input("How many people do you want to add to this file?"))
    address_book = open("address.txt", "w")
    for person in range(0, number):
        name = input("What is the name of person?")
        phone = input("What is their phone number?")
        email = input("What is there email address?")
        address_book.write(name + "," + phone + "," + email + "\n")
    address_book.close()

    
main()
