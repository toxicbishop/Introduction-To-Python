from datetime import date 

def cal_age(bday): 
    today = date.today() 
    age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day)) 
    return age 

Name = input("Enter name of a person: ") 
d = int(input("Enter day(dd) of birth: ")) 
m = int(input("Enter month(mm) of birth: ")) 
y = int(input("Enter year(yyyy) of birth: ")) 

age = cal_age(date(y, m, d)) 

if age < 0: 
    print("Enter Valid Date") 
elif age >= 60: 
    print("The person is Senior citizen") 
else: 
    print("The person is not Senior citizen") 