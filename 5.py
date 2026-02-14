fname = input('Enter the file name: ') 
try: 
    fhand = open(fname,"r") 
    counts = dict() 
    for line in fhand: 
        words = line.split() 
        for word in words: 
            if word in counts: 
                counts[word] += 1 
            else: 
                counts[word] = 1 
    counts=sorted(counts,reverse=True) 
    print(counts[:11]) 
     
except: 
    print("File can't open")