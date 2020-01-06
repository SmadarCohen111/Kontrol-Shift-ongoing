
class elal_emp:

  string = employe_name = " "
  employee_number =  0
  skills = {"ground_attendant": 0, "s_s": 0, "Team_leader": 0}
  seniority = 0

  def __init (self, employee_number):
      self.employee_number = employee_number

p1 = elal_emp()
check_arr = [["smadar cohen", 58719,2, 1, 1, 0 ],["Hagay tik", 28719, 3, 1, 1,1]]
rows = 2
columns = 1

p2 = elal_emp()

def skills():
  for x in p1.skills:
   if p1.skills[x] == 1:
       print(p1.skills)

def name_employee(check_arr):
    for i in range(rows):
       for j in range(columns):
        if(type(check_arr[i][j]) == str):
           p1.employe_name = check_arr[i][j]
           print(p1.employe_name, " is qualified to be")
           skills()


def check_seniority(check_arr):
    for i in range(2):
        for j in range(3):
            if(check_arr[i][j] != str and len(str(check_arr[i][j])) <= 2):
             p1.seniority = check_arr[i][j]
             print(p1.seniority)
            if p1.seniority < 0.6:
              for i in range (rows_1):
                  for j in range (columns_1):
                      p2.skills["ground_attendant"] = 1
                      name_employee(check_arr)





rows_1 = 1
columns_1 = 1
if check_arr.__sizeof__() != 0:
   # p2.seniority = (int),check_seniority(check_arr)
         check_seniority(check_arr)
         if p2.seniority < 0.6:
          for i in range(rows_1):
           for j in range(columns_1):
             p2.skills["ground_attendant"] = 1
             name_employee(check_arr)
      #   elif p2.seniority > 0.6:
            #skills()














