class Complex(): 
    def __init__ (self,r,i): 
        self.real = r   
        self.imag = i  
         
    def addcom(self, other): 
        return Complex(self.real + other.real, self.imag + other.imag) 
 
N=int(input("Enter a number of complex numbers: ")) 
sum=Complex(0,0) 
for i in range(N): 
    print("\nComplex Number:",i+1) 
    a=int(input("Enter real part: ")) 
    b=int(input("Enter imaginary part: ")) 
    c=Complex(a,b) 
    sum=sum.addcom(c) 
 
print("\nAfter Sum:",sum.real,"+",sum.imag,"i")