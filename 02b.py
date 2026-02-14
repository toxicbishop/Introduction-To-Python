def factorial(n): 
    if n == 0: 
        return 1 
    else: 
        return n * factorial(n-1) 
 
N = int(input("Enter a value for N: ")) 
R = int(input("Enter a value for R: ")) 
 
if R == 1 or R == N: 
    print(1) 
elif R > N: 
    print(0)         
else: 
    b_coef=factorial(N)/( factorial(N-R) * factorial(R) ) 
    print(b_coef)