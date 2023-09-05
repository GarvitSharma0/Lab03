class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

employees = [
    Employee("161E90", "Raman", 41, 56000),
    Employee("161F91", "Himadri", 38, 67500),
    Employee("161F99", "Jaya", 51, 82100),
    Employee("171E20", "Tejas", 30, 55000),
    Employee("171G30", "Ajay", 45, 44000)
]

def search_by_age(employees, operator, age):
    results = []
    for employee in employees:
        if operator == ">" and employee.age > age:
            results.append(employee)
        elif operator == "<" and employee.age < age:
            results.append(employee)
        elif operator == ">=" and employee.age >= age:
            results.append(employee)
        elif operator == "<=" and employee.age <= age:
            results.append(employee)
    return results

def search_by_salary(employees, operator, salary):
    results = []
    for employee in employees:
        if operator == ">" and employee.salary > salary:
            results.append(employee)
        elif operator == "<" and employee.salary < salary:
            results.append(employee)
        elif operator == ">=" and employee.salary >= salary:
            results.append(employee)
        elif operator == "<=" and employee.salary <= salary:
            results.append(employee)
    return results

def search_by_employee_id(employees, emp_id):
    results = []
    for employee in employees:
        if employee.emp_id == emp_id:
            results.append(employee)
    return results

while True:
    print("\nOptions:")
    print("1. Search by Age")
    print("2. Search by Salary")
    print("3. Search by Employee ID")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        operator = input("Enter operator (> < >= <=): ")
        age = int(input("Enter age: "))
        results = search_by_age(employees, operator, age)
    elif choice == "2":
        operator = input("Enter operator (> < >= <=): ")
        salary = int(input("Enter salary: "))
        results = search_by_salary(employees, operator, salary)
    elif choice == "3":
        emp_id = input("Enter Employee ID: ")
        results = search_by_employee_id(employees, emp_id)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
        continue
    
    if not results:
        print("No matching records found.")
    else:
        print("Matching Records:")
        for result in results:
            print(f"Employee ID: {result.emp_id}, Name: {result.name}, Age: {result.age}, Salary: {result.salary}")
