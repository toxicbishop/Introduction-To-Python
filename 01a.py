print("Enter Student details: ") 
Name=input("Enter a Name: ") 
USN=input("Enter USN: ") 
sub1=int(input("Enter marks of the first subject: ")) 
sub2=int(input("Enter marks of the second subject: ")) 
sub3=int(input("Enter marks of the third subject: ")) 
total=sub1+sub2+sub3 
Per=(total/300)*100 
print("Student details: ") 
print("Name: ",Name) 
print("USN: ",USN) 
print("Total Marks: ",total) 
print("Percentage: ",Per) 