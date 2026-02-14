infile = input("Enter input file name: ") 
fh_in = open(infile,"r") 
data=fh_in.readlines() 
lst = []  
for i in range(len(data)): 
    lst.append(data[i].strip()) 
lst.sort() 
fh_in.close() 
outfile=input("Enter output file name: ") 
fh_out = open(outfile, "w") 
for i in lst: 
    fh_out.write(i) 
    fh_out.write("\n") 
fh_out.close() 