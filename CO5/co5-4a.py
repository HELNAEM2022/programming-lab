import csv
with open("fruit1.csv",'w',newline='') as file:
  write=csv.writer(file)
  write.writerow(["Sl.No","fruits","rate"])
  write.writerow(["1","Mango","60"])
  write.writerow(["2","Papaya","50"])
  write.writerow(["3","grapes","60"])
  write.writerow(["4","Kiwi","75"])

  
with open("fruit1.csv" ,'r') as file:
    data=csv.reader(file)
    print("Contents in Column 'fruit': ")
    for r in data:
        print(r[1])
