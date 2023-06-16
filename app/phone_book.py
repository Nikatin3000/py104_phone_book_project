from contact import *

class PhoneBook:
    __slots__ = ('contacts',)

    def __init__(self, contacts=None):
        if contacts is None:
            self.contacts = []
        else:
            self.contacts = contacts

    def add_contact(self, contact=None):

        existing_contact = self.search_contact(contact.phone_number)

        if existing_contact:
            # Contact already exists, give user options
            print("Contact already exists. Choose an option:")
            print("1. Remove old contact and create new one")
            print("2. Edit contact")
            print("3. Cancel creation of new contact")
            option = input("Enter option number: ")

            if option == "1":
                self.remove_contact(existing_contact.phone_number)
                self.contacts.append(contact)
                print("New contact was added successfully.")

            elif option == "2":
                self.edit_contact(existing_contact.phone_number, contact)
                print("Contact was edited successfully.")
            else:
                print("Creation of the new contact was cancelled.")
        else:
            self.contacts.append(contact)
            print("Contact was added successfully.")

    def remove_contact(self, contact=None):
        pass

    def find_contact(self, contact=None):

        print("Input searching parameter "
              "(phone_number, name, surname, locality, email or social_media): '")
        option = input("Enter searching parameter: ")
        i = 0
        for cont in self.contacts:
            if cont['phone_number'] == option:
                print(cont)
            if cont['name'].lower() == option.lower():
                print(cont)
            if cont['surname'].lower() == option.lower():
                print(cont)
            if cont['locality'].lower() == option.lower():
                print(cont)
            if cont['email'].lower() == option.lower():
                print(cont)
            if cont['social_media'].lower() == option.lower():
                print(cont)
            else:
                i += 1
        if i == len(self.contacts):
            print('Nothing found')

