# Contact Book using Dictionary

contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = phone
        print("Contact added successfully.")

def search_contact():
    name = input("Enter Name to Search: ")

    if name in contacts:
        print("Name:", name)
        print("Phone:", contacts[name])
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter Name to Update: ")

    if name in contacts:
        new_phone = input("Enter New Phone Number: ")
        contacts[name] = new_phone
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter Name to Delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def display_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for name, phone in contacts.items():
            print(name, ":", phone)

# Main Menu
while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid choice! Please try again.")