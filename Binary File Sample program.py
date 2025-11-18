import pickle
def input_data():
    f = open("Reords.dat", "ab")
    l = []
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    roll = (input("Enter roll number: "))
    l.append(name)
    l.append(age)
    l.append(roll)
    pickle.dump(l, f)
    f.close()
def display_data():
    f = open("Reords.dat", "rb")
    print("The records in the file are:")
    try:
        while True:
            r = pickle.load(f)
            print("Name:", r[0], " Age:", r[1], " Roll Number:", r[2])
    except EOFError:
        pass
    f.close()
def update_data():
    f = open("Reords.dat", "rb")
    records = []
    try:
        while True:
            r = pickle.load(f)
            records.append(r)
    except EOFError:
        pass
    f.close()
    roll_to_update = (input("Enter roll number of the record to update: "))
    for record in records:
        if record[2] == roll_to_update:
            print("Current Record - Name:", record[0], " Age:", record[1], " Roll Number:", record[2])
            record[0] = input("Enter new name: ")
            record[1] = int(input("Enter new age: "))
            print("Record updated.")
            break
    else:
        print("Record not found.")
        return
    f = open("Reords.dat", "wb")
    for record in records:
        pickle.dump(record, f)
    f.close()
def delete_data():
    f = open("Reords.dat", "rb")
    records = []
    try:
        while True:
            r = pickle.load(f)
            records.append(r)
    except EOFError:
        pass
    f.close()
    roll_to_delete = (input("Enter roll number of the record to delete: "))
    records = [record for record in records if record[2] != roll_to_delete]
    f = open("Reords.dat", "wb")
    for record in records:
        pickle.dump(record, f)
    f.close()
    print("Record deleted if it existed.")
def main():
    while True:
        print("\nMenu:")
        print("1. Add Records")
        print("2. Display Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            input_data()
        elif choice == 2:
            display_data()
        elif choice == 3:
            update_data()
        elif choice == 4:
            delete_data()
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()
