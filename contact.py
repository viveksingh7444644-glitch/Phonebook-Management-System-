import json  # To work with JSON files

# The file where contacts will be stored
FILE_NAME = 'contacts.json'


def load_contacts():
    """
    Loads contacts from the JSON file.
    Uses exception handling for missing or corrupt files.
    """
    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)

    except FileNotFoundError:
        return []  # File missing → return empty list

    except json.JSONDecodeError:
        print("Warning: Could not read contact file. Starting fresh.")
        return []  # File corrupted → return empty list


def save_contacts(contacts):
    """Saves the contact list back to the JSON file."""
    with open(FILE_NAME, 'w') as f:
        json.dump(contacts, f, indent=2)


def find_contact(contacts, name):
    """Finds a contact by name (case-insensitive)."""
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            return contact
    return None


# --- Main Program ---
def main():
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

        # ADD CONTACT
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contacts.append({'name': name, 'phone': phone, 'email': email})
            save_contacts(contacts)
            print(f"Success: Contact for {name} added.")

        # VIEW ALL CONTACTS
        elif choice == '2':
            if not contacts:
                print("Your contact book is empty.")
            else:
                print("\n--- All Contacts ---")
                for contact in contacts:
                    print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

        # SEARCH CONTACT
        elif choice == '3':
            search_name = input("Enter name to search: ")
            found = False

            for contact in contacts:
                if search_name.lower() in contact['name'].lower():
                    print(f"Found → {contact['name']}, {contact['phone']}, {contact['email']}")
                    found = True

            if not found:
                print(f"No contacts found matching '{search_name}'.")

        # UPDATE CONTACT
        elif choice == '4':
            name = input("Enter the exact name of the contact to update: ")
            contact_to_update = find_contact(contacts, name)

            if contact_to_update:
                print(f"Updating {name}. Press Enter to keep the old value.")

                new_phone = input(f"New phone ({contact_to_update['phone']}): ")
                new_email = input(f"New email ({contact_to_update['email']}): ")

                if new_phone:
                    contact_to_update['phone'] = new_phone
                if new_email:
                    contact_to_update['email'] = new_email

                save_contacts(contacts)
                print(f"Success: Contact for {name} updated.")

            else:
                print(f"Error: Contact '{name}' not found.")

        # DELETE CONTACT
        elif choice == '5':
            name = input("Enter the exact name of the contact to delete: ")
            contact_to_delete = find_contact(contacts, name)

            if contact_to_delete:
                contacts.remove(contact_to_delete)
                save_contacts(contacts)
                print(f"Success: Contact for {name} has been deleted.")
            else:
                print(f"Error: Contact '{name}' not found.")

        # EXIT PROGRAM
        elif choice == '6':
            print("Exiting. Your contacts are saved.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 6.")


# Run the program
if __name__ == "__main__":
    main()
