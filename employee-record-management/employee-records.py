employees = []

while True:
    print("\n===== EMPLOYEE RECORD MANAGEMENT =====")
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

        employee = {
            "id": emp_id,
            "name": name,
            "department": department,
            "salary": salary
        }

        employees.append(employee)
        print("Employee added successfully!")

    elif choice == "2":
        if not employees:
            print("No employee records found.")
        else:
            print("\n===== EMPLOYEE RECORDS =====")

            for employee in employees:
                print("Employee ID :", employee["id"])
                print("Name        :", employee["name"])
                print("Department  :", employee["department"])
                print("Salary      :", employee["salary"])
                print("----------------------------")

    elif choice == "3":
        search_id = input("Enter Employee ID to search: ")
        found = False

        for employee in employees:
            if employee["id"] == search_id:
                print("\nEmployee Found!")
                print("Employee ID :", employee["id"])
                print("Name        :", employee["name"])
                print("Department  :", employee["department"])
                print("Salary      :", employee["salary"])
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == "4":
        print("Thank you for using Employee Record Management.")
        break

    else:
        print("Invalid choice.")
