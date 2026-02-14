import sys 
def DivExp(a,b): 
    try: 
        assert a>0, "Expected number should be positive" 
        assert b!=0, "Can't divide by zero" 
        c=a/b 
        return c 
    except AssertionError as msg: 
        sys.exit(msg) 
         
v1=int(input("Enter first number: ")) 
v2=int(input("Enter second number: ")) 
res=DivExp(v1,v2) 
print(v1,"%",v2," is: ",res)