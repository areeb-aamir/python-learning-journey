contacts = {}

def add_contact(contacts, name, number):
    next_id = len(contacts) + 1
    contacts[next_id] = {"Name":name, "Number":number}



def search_contact(contacts, name):
    for id, contact in contacts.items():
        if contact["Name"] == name:
            print(f"Name : {contact['Name']} - Phone Number : {contact['Number']}")
            return
    print("Contact Not Found!")



def delete_contact(contacts, name):
    for id, contact in contacts.items():
        if contact["Name"] == name:
            del contacts[id]
            return
    print("Contact Not Found!")


def show_all(contacts):
    for id, contact in contacts.items():
        print(f"ID : {id}")
        print(f"Name : {contact['Name']}")
        print(f"Phone Number : {contact['Number']}")


