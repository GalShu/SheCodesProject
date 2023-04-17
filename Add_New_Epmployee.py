# import csv

# file = open('Employees.csv','r')
# csvreader = csv.reader(file)
# header = []
# header = next(csvreader)
# print(header)
#
# #print (header)
#
# rows = []
# for row in csvreader:
#        rows.append(row)
# print(rows)
#
# reader = csv.DictReader(file)
# for row in reader:
#       print(row)
#
#
import pandas as pd
from validation import *

def Add_New_Emmployee ():
    dataEmployees= pd.read_csv('Employees.csv')
    # print(dataEmployees)
    # print(dataEmployees.columns)
    # print(dataEmployees.Name)



    # Employees=dict()
    Valid=False
    while Valid==False:                                         #input ID for add new employee
        ID = input('For add new employee, Please write ID:\n')
        if CheckID(ID):
            ValidForDup = False
            while ValidForDup == False:  # check if the ID exsists
                if CheckDuplicate(dataEmployees, ID):
                    ValidForDup = True
                    Valid = True
                else:
                    print('The employee already exists')
                    break
        else:
            print ('The ID is incorrect')
        # CheckDuplicate(dataEmployees, ID)    #to add duplicate test




    Valid=False
    while Valid==False:                                         #input Name of employee
        EmpName = input('Please write employee name:\n')
        if CheckName(EmpName):
            Valid=True
        else:
            print ('The Name is wrong')

    Valid=False
    while Valid==False:                                         #input Phone
        Phone = input('Please write Phone Number:\n')
        if CheckPhoneNumber(Phone):
            Valid=True
        else:
            print ('The number is incorrect')

    Valid=False
    while Valid==False:                                         #input Phone
        Age = input('Please write age:\n')
        if CheckAge(Age):
            Valid=True
        else:
            print ('The Age is incorrect')
    # Employees[ID]=[EmpName,Phone,Age]



    Employee =pd.DataFrame( {
      "ID": [ID],
      "EmpName": [EmpName],
      "Phone":[Phone],
      "Age":[Age]
    })
    # print (Employee)
    dataEmployees=pd.concat([dataEmployees,Employee], ignore_index=True)
    dataEmployees=dataEmployees.loc[:, ~dataEmployees.columns.str.match('Unnamed')]
    print(dataEmployees)
    dataEmployees.to_csv('Employees.csv')

def Add_New_Emmployee_from_file ():
    Valid = False
    while Valid == False:  # input Path_File for add new employees
        Path_File = input('For add new employees from file, Please write the path of the file:\n')
        if CheckPath(Path_File):
            Valid = True
        else:
            print('The path is incorrect')
#C:\Users\morad\OneDrive - HP Inc\Desktop\gal\she codes\new_employees.csv
    dataEmployeesFromFile = pd.read_csv(Path_File)

    print (dataEmployeesFromFile)
    print (dataEmployeesFromFile.columns)


#Add_New_Emmployee_from_file()
Add_New_Emmployee()

