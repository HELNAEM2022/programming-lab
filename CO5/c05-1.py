str1="Welcome to python programming""\n""python""\n"
fw=open("file.txt","w")
fw.write(str1)
fw.close()
fr=open("file.txt","r")
str2=fr.readlines()
for i in str2:
     print(i)
