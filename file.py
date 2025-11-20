import json  # We need this module to work with 
JSON files 
# The name of the file where we'll store contacts 
FILE_NAME = 'contacts.json' 
def load_contacts(): 
""" 
Loads contacts from the JSON file. 
Uses exception handling for missing or corrupt 
f
 iles. 
""" 
try: 
# 'r' means read-only 
with open(FILE_NAME, 'r') as f: 
            return json.load(f) 
    except FileNotFoundError: 
        # If the file doesn't exist, return an empty list 
        return [] 
    except json.JSONDecodeError: 
        # If the file is empty or corrupt, return an 
empty list 
        print("Warning: Could not read contact file. 
Starting fresh.") 
        return [] 
 
def save_contacts(contacts): 
    """Saves the entire contact list back to the JSON 
file.""" 
    # 'w' means write (it will overwrite the old file) 
    with open(FILE_NAME, 'w') as f: 
        # json.dump writes the list to the file, 
indent=2 makes it readable 
        json.dump(contacts, f, indent=2) 
 
def find_contact(contacts, name): 
    """Helper function to find the first contact that 
matches a name.""" 
    for contact in contacts: 
        # .lower() makes the search case-insensitive 
        if contact['name'].lower() == name.lower(): 
            return contact 
    return None 
 
# --- Main Program --- 
def main(): 
    # Load contacts from the file right at the start 
    contacts = load_contacts() 
 
    while True: 
        print("\n--- File-Based Contact Book ---") 
        print("1. Add a new contact") 
        print("2. View all contacts") 
        print("3. Search for a contact") 
        print("4. Update a contact") 
        print("5. Delete a contact") 
        print("6. Exit") 
        choice = input("Enter your choice (1-6): ") 
 
        if choice == '1':  # Add 
            name = input("Enter name: ") 
            phone = input("Enter phone: ") 
            email = input("Enter email: ") 
            contacts.append({'name': name, 'phone': 
phone, 'email': email}) 
            save_contacts(contacts) 
            print(f"Success: Contact for {name} added.") 
 
        elif choice == '2':  # View All 
            if not contacts: 
                print("Your contact book is empty.") 
            else: 
                print("\n--- All Contacts ---") 
                for contact in contacts: 
                    # Neatly formatted output using f
strings 
                    print(f"  Name: {contact['name']}, 
Phone: {contact['phone']}, Email: 
{contact['email']}") 
 
        elif choice == '3':  # Search 
            search_name = input("Enter name to 
search: ") 
            found = False 
            for contact in contacts: 
                if search_name.lower() in 
contact['name'].lower(): 
                    print(f"  Found: {contact['name']}, 
{contact['phone']}, {contact['email']}") 
                    found = True 
            if not found: 
                print(f"No contacts found matching 
'{search_name}'.") 
 
        elif choice == '4':  # Update 
            name = input("Enter the exact name of the 
contact to update: ") 
            contact_to_update = find_contact(contacts, 
name) 
             
            if contact_to_update: 
                print(f"Updating {name}. Press Enter to 
keep the old value.") 
                new_phone = input(f"New phone 
({contact_to_update['phone']}): ") 
                new_email = input(f"New email 
({contact_to_update['email']}): ") 
                 
                if new_phone: 
                    contact_to_update['phone'] = 
new_phone 
                if new_email: 
                    contact_to_update['email'] = 
new_email 
                     
                save_contacts(contacts) 
                print(f"Success: Contact for {name} 
updated.") 
            else: 
                print(f"Error: Contact '{name}' not 
found.") 
 
        elif choice == '5':  # Delete 
            name = input("Enter the exact name of the 
contact to delete: ") 
            contact_to_delete = find_contact(contacts, 
name) 
             
            if contact_to_delete: 
                contacts.remove(contact_to_delete) 
                save_contacts(contacts) 
                print(f"Success: Contact for {name} has 
been deleted.") 
            else: 
                print(f"Error: Contact '{name}' not 
found.") 
 
        elif choice == '6':  # Exit 
            print("Exiting. Your contacts are saved.") 
            break 
         
        else: 
            print("Invalid choice. Please select from 1
6.") 
 
# This standard line runs the main() function when 
you start the script 
if __name__ == "__main__": 
    main() 
