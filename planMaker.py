import json as js
import random as rd

def getEmployeesNames(hoursNeeded):
    with open('employeesHoursPerWeek.json', 'r') as file:
        data = js.load(file)
    data = data['employees']
    names = []
    for i in range(len(data)):
        if data[i]['hours_per_week'] == hoursNeeded:
            names.append(data[i]['name'] + ' ' + data[i]['last_name'])
        
    return names

def getHoursshifts():
    with open('hoursOpening.json') as file:
        data = js.load(file)
    print(data)
    return data

def displayWeeks(employees, daysOff):
    for i in range(len(employees)):
        for j in range(4):
            print(employees[i], " Week ", j+1, " day off -> ", daysOff[i][j])
        print("")

def setEmployeesDaysOff35():
    employees = getEmployeesNames(35)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    daysOff = []
    employeeDayOff = []
    for i in range(len(employees)):
        idRand = rd.randint(0,3)
        for j in range(4):
            if j == idRand:
                employeeDayOff.append('Saturday')
            else:
                employeeDayOff.append(days[rd.randint(0, len(days)-1)])
        daysOff.append(employeeDayOff)
        employeeDayOff = []
    
    displayWeeks(employees, daysOff)
    return daysOff

def setEmployeesDaysOff30():
    employees = getEmployeesNames(30)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    daysOff = []
    employeeDayOff = []
    for i in range(len(employees)):
        idRand = rd.randint(0,3)
        for j in range(4):
            if j == idRand:
                employeeDayOff.append('Saturday')
            else:
                employeeDayOff.append(days[rd.randint(0, len(days)-1)])
        daysOff.append(employeeDayOff)
        employeeDayOff = []
    
    displayWeeks(employees, daysOff)
    return daysOff

def setEmployeesDaysOff24():
    employees = getEmployeesNames(24)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    daysOff = []
    subDaysOff = []
    employeeDayOff = []
    for i in range(len(employees)):
        idRand = rd.randint(0,3)
        for j in range(4):
            saturdayHappened = False
            for i in range(2):
                if j == idRand and not saturdayHappened:
                    subDaysOff.append('Saturday')
                    saturdayHappened = True
                else:
                    daysDifferent = False
                    while not daysDifferent:
                        dayChosen = days[rd.randint(0, len(days)-1)]
                        if len(subDaysOff) == 1 and dayChosen == subDaysOff[0]:
                            continue
                        else:
                            subDaysOff.append(dayChosen)
                            daysDifferent = True
            employeeDayOff.append(subDaysOff)
            subDaysOff = []
        daysOff.append(employeeDayOff)
        employeeDayOff = []
    
    displayWeeks(employees, daysOff)
    return daysOff

def daysShift(employees, daysOff, hours):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    shifts = []
    hoursShifts = getHoursshifts()
    for i in range(len(employees)):
        weekDaysShifts = []
        for j in range(2):
            daysDifferent = False
            while not daysDifferent:
                daysS = days[rd.randint(0, 3)]
                if len(weekDaysShifts) == 1 and daysS == weekDaysShifts[0]:
                    continue
                else:
                    weekDaysShifts.append(daysS)
                    daysDifferent = True
        month = []
        for k in range(4):
            week = []
            for h in range(6):
                match hours:
                    case 35:
                        if days[h] == daysOff:
                            week.append({'start':'N/A','end':'N/A'})
                        elif k in weekDaysShifts:
                            week.append(hoursShifts['dayShift'])
                        else:
                            week.append(hoursShifts['nightShift'])
                        break
                    case 30:
                        if days[h] == daysOff:
                            week.append({'start':'N/A','end':'N/A'})
                        elif k in weekDaysShifts:
                            week.append(hoursShifts['partDayShift'])
                        else:
                            week.append(hoursShifts['partNightShift'])
                        break
                    case 24:
                        if days[h] in daysOff:
                            week.append({'start':'N/A','end':'N/A'})
                        elif k in weekDaysShifts:
                            week.append(hoursShifts['partDayShift'])
                        else:
                            week.append(hoursShifts['partNightShift'])
                        break
            month.append(week)
            week = []
        weekDaysShifts = []
        shifts.append(month)
    print(shifts)
    print('\n')
    return shifts

def shiftDisplay(employees, shifts):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for i in range(len(employees)):
        print(employees[i], ": ")
        for j in range(len(shifts[i])):
            print("Week ", j+1, ": ")
            for k in range(len(shifts[i][j])):
                print("-> ", days[k], ": ", shifts[i][j][0]['start'], " - ", shifts[i][j][0]['end'])
            print()
        print()



def shiftGiver():
    fullWorkers = getEmployeesNames(35)
    partWorkers = getEmployeesNames(30)
    partPlusWorkers = getEmployeesNames(24)

    daysOff35 = setEmployeesDaysOff35()
    daysOff30 = setEmployeesDaysOff30()
    daysOff24 = setEmployeesDaysOff24()

    shiftDisplay(fullWorkers, daysShift(fullWorkers, daysOff35, 35))


#setEmployeesDaysOff35()
#print('\n')
#setEmployeesDaysOff30()
#print('\n')
#setEmployeesDaysOff24()

shiftGiver()