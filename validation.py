def CheckID(ID) :
    if((len(ID)==9) and ID.isnumeric()):
        return True
    else:
        return False

    # IdList = list()

    # try :
    # 	id = list(map(int, ID))
    # except :
    # 	return False

    # counter = 0
    #
    # for i in range(9) :
    # 	id[i] *= (i%2) +1
    # 	if(id[i]>9) :
    # 		id[i] -=9
    # 	counter += id[i]
    #
    # if(counter%10 == 0) :
    # 	return True
    # else :
    # 	return False

print(CheckID("201437183"))

def CheckPhoneNumber(Phone) :
    if (len(Phone) != 10 and Phone.isnumeric()):
        return False

    if Phone[0]=='0':
        return True
    else:
        return False

# print(CheckPhoneNumber("0525547563"))

def CheckAge(Age):

    if (Age.isnumeric()):
        if (int(Age)>18 and int(Age)<67 ):
            return True
        else:
            return False
    else:
        return False

# print(CheckAge("22"))

def CheckName(Name):
    if (Name.isalpha()):
            return True
    else:
        return False

#print(CheckName(' '))

def CheckDuplicate(Employees,ID):
    print(Employees['ID'].values)
    #if ((ID in Employees.values)):
    if (Employees['ID'].isin([ID])):
        print('False')
        return False
    else:
        print('True')
        return True

# import os.path
from os import path

def CheckPath(Path_File):
    if path.exists(Path_File):
        # print('True')
        return True
    else:
        # print('False')
        return False

#CheckPath('C:\\Users\\morad\\OneDrive - HP Inc\\Desktop\\gal\\she codes\\new_employees.txt')
