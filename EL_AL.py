import numpy as np


class elal_emp:
    employee_name = " "
    employee_number = 0
    skills = {"ground_attendant": False, "s_s": False, "Team_leader": False}
    seniority = 0

    def __init(self, employee_name, employee_number):
        self.employee_name = employee_name
        self.employee_number = employee_number


p1 = elal_emp()
check_arr = [["Smadar cohen", 58719, 2, True, True, False], ["Hagay tik", 28719, 3, True, True, True]]

def print(skills):

def skills(check_arr):
    for i in range(len(check_arr)):
        for j in range(6):
            if(type(check_arr[i][j]) == bool):
                p1.skills[j] = check_arr[i][j]
                print()



def name_employee(check_arr):
    for i in range(len(check_arr)):
       for j in range(len(check_arr)):
        if(type(check_arr[i][j]) == str):
           p1.employe_name = check_arr[i][j]
           print(p1.employe_name, " is qualified to be")
           skills(check_arr)


p2 = elal_emp()
p2.employee_name = name_employee(check_arr)