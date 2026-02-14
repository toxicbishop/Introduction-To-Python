import math 
 
n=int(input("Enter N value:")) 
Mylist=[] 
print("Enter a value") 
for i in range(n): 
    v=int(input()) 
    Mylist.append(v) 
lenv=len(Mylist) 
if(lenv == 0): 
    print("List should not be empty") 
else: 
    sumv=sum(Mylist) 
    meanval = sumv/lenv 
    temp=0 
    for i in range(lenv): 
        temp += ((Mylist[i] - meanval) * (Mylist[i] - meanval))  
    vari = temp / lenv; 
    sd = math.sqrt(vari) 
    print("Mean value: ",meanval) 
    print("Varience: ",vari) 
    print("Standard Deviation: ",sd)