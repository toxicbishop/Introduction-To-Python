str1 = input("Enter a multi-digit number: ") 
d = dict() 
for c in str1: 
    if c in d.keys(): 
        d[c] = d[c] + 1 
    else: 
        d[c] = 1 
for k,v in d.items(): 
    print("Number ",k," has frequency: ",v) 