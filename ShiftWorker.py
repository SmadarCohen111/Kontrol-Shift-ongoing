import mysql.connector
import numpy as np
from FlightsLast import T1


class ShiftWorker:
    queue_tl = []
    queue_at = []
    duty_mat = np.array([[]])
    check_before_setting = T1.num_of_teams


    def add_tl(self, obj):
        self.queue_tl.append(obj)

    def add_at(self, obj):
        self.queue_at.append(obj)


    """def calc_and_create_mat(self, team_leader, attendants, flight_mat, team_flights):
        if self.duty_mat is None or flight_mat is not None:  # first assignment for the tree
            self.duty_mat = [[0 for x in flight_mat*2] for y in flight_mat*2]
        self.fill(team_leader, flight_mat, 0, 0, 0, 0)

    def fill(self, team_leader, attendants, te):
        if self.duty_mat[self.duty_mat.__len__()-1][self.duty_mat.__len__()-1] != 0:
            return self.duty_mat
        if flight_mat[row_flight][col_flight] == 1:
            self.duty_mat[row_duty][col_duty] = team_leader[col_flight]
            self.fill(team_leader, flight_mat, row_duty, col_duty+2, row_flight, col_flight+1)
        elif flight_mat[row_flight][col_flight] == 0 and row_flight == 0:
            self.duty_mat[row_duty][col_duty] = team_leader[col_duty-(col_flight*2)]
            self.fill(team_leader, flight_mat, col_duty, 0, col_flight+1, 0)
        elif flight_mat[row_flight][col_flight] == 0 and row_flight != 0:
            self.duty_mat[row_duty][col_duty] = self.duty_mat[row_duty][col_flight]
            col_flight += 2
            self.fill(team_leader, flight_mat, row_duty, col_duty+2, row_flight, col_flight)

"""

    def fill(self, team_leader, attendants, team_flights):
        team_flights.add_team_members(team_leader, attendants)
        #print(team_flights)

    def check(self, teamlea, atte):
        if teamlea.__len__() >= self.check_before_setting:
            print("We have enough team leader")
        else:
            print("We dont have enough team leader")
        if atte.__len__() >= self.check_before_setting:
            print("We have enough attendants")
        else:
            print("We dont have enough attendants")

conn = mysql.connector.connect(host='localhost',
                               database='ground_attendant',
                               user='root',
                               password='smadar')

cursor = conn.cursor(buffered=True)
attendant = conn.cursor(buffered=True)


cursor.execute(
    '''select
    firstName,
    lastName,
    groundAttendantId,
    startShift,
    endShift,
    date
    from worker_shift as w, attendants_details as ad
    where ad.employeeNumber = w.groundAttendantId and w.startShift = "11:00"
       and w.TeamLeader = 1
    '''
)


attendant.execute(
    '''select
    firstName,
    lastName,
    groundAttendantId,
    startShift,
    endShift,
    date
    from worker_shift as ws, attendants_details as a
    where a.employeeNumber = ws.groundAttendantId and ws.startShift = "11:00"
       and ws.attendant = 1
    '''
)
attendants = attendant.fetchall()
team_leader_result = cursor.fetchall()


def sort_by_boarding(flights):
    return flights[1]


num_of_emp_on_flights = conn.cursor()

num_of_emp_on_flights.execute('''select flightNum,boardingTime,attendants,teamLeader,tsa
                                  from flights
                                  where boardingTime > 11 and boardingTime < 17''')
help_build_the_mat = num_of_emp_on_flights.fetchall()

s = ShiftWorker()
for i in team_leader_result:
    s.add_tl(i)

for i in attendants:
    s.add_at(i)

s.fill(s.queue_tl, s.queue_at, T1.team_flights)
print(s.duty_mat)

