#creating a form accepting name and email from user and storing it in a file and doing basic validation, updation, deletion, display of records
import re
def is_valid_email(email):
    # Basic email validation using regex
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
def add_record(name, email):
    if not is_valid_email(email):
        print("Invalid email format.")
        return
    with open('records.txt', 'a') as f:
        f.write(f"{name},{email}\n")
    print("Record added successfully.")
def display_records():
    try:
        with open('records.txt', 'r') as f:
            records = f.readlines()
            if not records:
                print("No records found.")
                return
            for record in records:
                name, email = record.strip().split(',')
                print(f"Name: {name}, Email: {email}")
    except FileNotFoundError:
        print("No records found.")
def update_record(old_email, new_name, new_email):
    if not is_valid_email(new_email):
        print("Invalid email format.")
        return
    try:
        with open('records.txt', 'r') as f:
            records = f.readlines()
        with open('records.txt', 'w') as f:
            found = False
            for record in records:
                name, email = record.strip().split(',')
                if email == old_email:
                    f.write(f"{new_name},{new_email}\n")
                    found = True
                else:
                    f.write(record)
            if found:
                print("Record updated successfully.")
            else:
                print("Record not found.")
    except FileNotFoundError:
        print("No records found.")
def delete_record(email):
    try:
        with open('records.txt', 'r') as f:
            records = f.readlines()
        with open('records.txt', 'w') as f:
            found = False
            for record in records:
                name, rec_email = record.strip().split(',')
                if rec_email == email:
                    found = True
                else:
                    f.write(record)
            if found:
                print("Record deleted successfully.")
            else:
                print("Record not found.")
    except FileNotFoundError:
        print("No records found.")
def main():
    while True:
        print("\nMenu:")
        print("1. Add Record")
        print("2. Display Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_record(name, email)
        elif choice == '2':
            display_records()
        elif choice == '3':
            old_email = input("Enter the email of the record to update: ")
            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")
            update_record(old_email, new_name, new_email)
        elif choice == '4':
            email = input("Enter the email of the record to delete: ")
            delete_record(email)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()