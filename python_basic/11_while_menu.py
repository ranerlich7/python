my_contacts = []

def add_contact(my_arr):
    new_contact = input("please enter name of new contact:")
    my_arr.append(new_contact)

def menu():
    while True:
        print('1 - Add Contact')
        print('2 - Edit Contact')
        print('3 - Delete Contact')
        print('4 - List of all contacts')
        print('5 - Exit')
        selection = input("please enter command:")
        if (selection == "1"):
            add_contact(my_contacts)
        if (selection == "5"):
            break

menu()
