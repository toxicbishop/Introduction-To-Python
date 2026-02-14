N = int(input("Enter N value: ")) 
n1, n2 = 0, 1 
count = 0 
if N <= 0: 
   print("Please enter a positive integer") 
elif N == 1: 
   print("Fibonacci sequence upto",N,":") 
   print(n1) 
else: 
   print("Fibonacci sequence:") 
   while count < N: 
       print(n1) 
       nxt = n1 + n2 
       n1 = n2 
       n2 = nxt 
       count += 1  # count++ 