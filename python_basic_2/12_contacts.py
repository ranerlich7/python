my_contacts = [
    {"name": "ran", "phone": "05055555", "age": 44},
    {"name": "itzik", "phone": "555666", "age": 25},
    {"name": "avraham", "phone": "2345345", "age": 22}
    ]
# exmaple of array within array
# my_contacts = [["ran","05055555",44], ["ran erlich","555-242442",44], ["itzik","555666",25]]

# 1. menu function
# 2. add contact
# 3. delete contact
# 4. search contact


def add_contact():
    print("****** in add_contact")
    new_contact_name = input("Please enter new contact name:")
    new_contact_phone = input("Please enter new contact phone:")
    new_contact_age = int(input("Please enter new contact age:"))
    new_contact = {"name":new_contact_name, 
                   "phone":new_contact_phone, 
                   "age":new_contact_age}
    my_contacts.append(new_contact)
    print("****** added succesfuly")


def search():
    print("!!!! search entered")
    search_str = input("Please enter search str:")
    found = False
    for contact in my_contacts:
        if (
            search_str.lower() in contact["name"].lower()  # search in name
            or search_str.lower() in contact["phone"].lower()  # search in phone number
            or search_str.lower() in str(contact["age"])  # search in age
        ):
            print(f"contact name:{contact["name"]}. phone:{contact["phone"]}. age:{contact["age"]}")
            found = True

    if not found:
        print("not found!")


def menu():
    while True:
        print("please choose an option:")
        print("1 - Add Contact")
        print("2 - Edit Contact")
        print("3 - Delete Contact")
        print("4 - List of all contacts")
        print("5 - Search")
        print("6 - Exit")
        selection = input("please enter command:")
        if selection == "1":
            add_contact()
        elif selection == "2":
            print("2 is selected")
        elif selection == "3":
            print("3 is selected")
        elif selection == "4":
            print(my_contacts)
        elif selection == "5":
            search()
        elif selection == "6":
            print("exit is selected")
            exit()


menu()
