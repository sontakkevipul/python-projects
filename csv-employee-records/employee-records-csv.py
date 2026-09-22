import csv

file_name = "employees.csv"

while True:
    print("\n===== CSV EMPLOYEE RECORD MANAGEMENT =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = input("Enter Salary: ")

        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([emp_id, name, department, salary])

        print("Employee record added successfully!")

    elif choice == "2":
        try:
            with open(file_name, "r", newline="") as file:
                reader = csv.reader(file)

                print("\n===== EMPLOYEE RECORDS =====")

                for row in reader:
                    print(
                        "ID:", row[0],
                        "| Name:", row[1],
                        "| Department:", row[2],
                        "| Salary:", row[3]
                    )

        except FileNotFoundError:
            print("No employee records found.")

    elif choice == "3":
        search_id = input("Enter Employee ID to search: ")
        found = False

        try:
            with open(file_name, "r", newline="") as file:
                reader = csv.reader(file)

                for row in reader:
                    if row[0] == search_id:
                        print("\nEmployee Found!")
                        print("Employee ID :", row[0])
                        print("Name        :", row[1])
                        print("Department  :", row[2])
                        print("Salary      :", row[3])

                        found = True
                        break

            if not found:
                print("Employee not found.")

        except FileNotFoundError:
            print("No employee records found.")

    elif choice == "4":
        print("Thank you for using CSV Employee Record Management.")
        break

    else:
        print("Invalid choice.")
