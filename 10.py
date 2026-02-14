class Student: 
    def __init__(self): 
        self.USN=input("Enter Student USN: ") 
        self.Name=input("Enter student name: ") 
        self.Marks=self.getMarks() 
     
    def getMarks(self): 
        mrk=[] 
        print("Enter the marks of subjects out of 100") 
        for i in range(3): 
            print("Subject",i+1) 
            m=int(input()) 
            mrk.append(m) 
        mrk.append(sum(mrk)) 
        return mrk 
         
    def display(self): 
        print("\nName: ",self.Name) 
        print("USN: ",self.USN) 
        print("----------------------------") 
        print("Subject 1 Marks: ",self.Marks[0]) 
        print("Subject 2 Marks: ",self.Marks[1]) 
        print("Subject 3 Marks: ",self.Marks[2]) 
        print("============================") 
        print("          Total: ",self.Marks[3]) 
        per=(self.Marks[3]/300)*100 
        print("----------------------------") 
        print("     percentage: ",per) 
         
print("Enter student Details: ") 
s=Student() 
s.display()