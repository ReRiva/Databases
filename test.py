
import pymysql as sql
import keyboard as kb
import db_functions as dbf

dbf.mysql_connect()

# Print the name of the employee and the department two names at the time and order by department name and the employee name.
def employee_department_menu():
    emp_dept = dbf.get_employee_department_info() 
    key = str(input("---Quit (q)---"))
    while key!= "q":
        for emp in emp_dept:
            print(emp["name"], "|", emp["d.name"])
            key = str(input("---Quit (q)---"))
        
        
    

### Function for the application menu

def application_menu(): 
    print("Employees\n"
        "---------\n\n"
        "Menu\n"
        "======\n"
        "1 - View Employees & Departments\n"
        "2 - View Salary Details\n"
        "3 - View by Month of Birth\n"
        "4 - Add new Employee\n"
        "5 - View Departments managed by Employee\n"
        "6 - Add Managers to Department\n"
        "7 - View Departments\n"
        "x - Exit the Application")
        
        
 

        

def main():
    application_menu()
    while True:    
        choice = input("Choice: ")
        if choice == "1":
            employee_department_menu()
            application_menu()
        elif choice == "2":
            print("Menu 2")
        elif choice == "3":
            print("Menu 3")
        elif choice == "4":
            print("Menu 4")
        elif choice == "5":
            print("Menu 5")
        elif choice == "6":
            print("Menu 6")
        elif choice == "7":
            print("Menu 7")
        elif choice == "x":
            print("Exiting the application")
            break
        else:
            application_menu()
            print("Please choose a valid option")
        

if __name__ == "__main__":
    main()
