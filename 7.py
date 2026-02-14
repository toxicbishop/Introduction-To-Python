import os 
import zipfile 
fold=input("Enter Directory name: ") 
#zipf = fold +".zip" 
#zf = zipfile.ZipFile(zipf, "w") 
zf = zipfile.ZipFile("myzipfile.zip", "w") 
for dirname, subdirs, files in os.walk(fold): 
 zf.write(dirname) 
for filename in files: 
        zf.write(os.path.join(dirname, filename)) 
zf.close()