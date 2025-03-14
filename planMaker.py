import json as js
import random as rd

def getEmployeesNames():
    with open('employeesHoursPerWeek.json', 'r') as file:
        data = js.load(file)
    data = data['employees']
    names = []
    for i in range(len(data)):
        names.append(data[i]['name'] + ' ' + data[i]['last_name'])
    return names

def displayWeeks(weeks):
    for i in range(len(weeks)):
        print('Week', i + 1, ": ")
        for j in range(len(weeks[i])):
            # Display the employee name and the day off cooresponding
            print(weeks[i][j])
        print()

def setEmployeesDaysOff():
    employees = getEmployeesNames()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    weeks = []
    daysOff = []
    for i in range(4):
        for i in range(len(employees)):
            daysOff.append({employees[i] : days[rd.randint(0, 5)]})
        weeks.append(daysOff)
        daysOff = []
    displayWeeks(weeks)
    return daysOff

setEmployeesDaysOff()