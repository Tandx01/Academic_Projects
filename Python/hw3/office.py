"""
Name: Taha Andac
ID : 75785
Section : 03"""

def add_employee(employee_list, name, phone, room):

    """Fuction takes a list of employees together with the name, phone number,
    and room number of an employee to be added. Fuction checks whether the name
    exits in employee list or not. If the name does not exist in the
    list, the function adds a tuple for the employee to the end of the list.
    Otherwise, if the name already exists in the list, the function does not add
    any tuple to the list and displays a warning message. """

    lower_case_name = name.lower()
    
    for i in employee_list:
        a = i[0].lower()
        if a == lower_case_name:
            print(f"(error in add), {name} already exists")
            return
        
    employee_list.append((name,phone,room))


def remove_employee(employee_list, name):

    """Function takes a list of employees together with the name of an employee
    to be removed. If the name exists in the list, the function removes the
    corresponding tuple from the list. Otherwise, if the name does not exist in
    the list, the function does not remove any tuple from the list and displays
    a warning message. """

    lower_case_name = name.lower()
    for i in employee_list:
        a = i[0].lower()
        if a == lower_case_name:
            index = employee_list.index(i)
            employee_list.pop(index)
            return employee_list

    print(f"(error in remove), {name} is not found")

def display_all(employee_list):

    """ This function takes a list of employees and displays all employee tuples
    found in the list according to the required output format. If there exist
    no tuples in the list, this function displays empty."""

    if len(employee_list)== 0:
        print ("---EMPTY---")
        return
    for i in employee_list:
        print(f"{i[0]} , {i[2]} , {i[1]}")


def show_employee(employee_list, name):

    """This function takes a list of employees together with the name of an employee
    whose information will be showed. If the name exists in the list, the function
    displays the information stored in the corresponding tuple according to the
    required output format. If the name does not exist in the list, it displays
    a warning message."""

    lower_case_name = name.lower()
    for i in employee_list:
        a = i[0].lower()
        if a == lower_case_name:
            print(f"Name: {i[0]} \nOffice: {i[2]} \nTel: {i[1]}")
            return
    print(f"(error in show) {name} is not found")

