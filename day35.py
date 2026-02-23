# import csv
# try:
#     with open("students.csv","r") as file:
#         reader=csv.reader(file)
#         # print(reader)
#         # print(list(reader))
#         for row in reader:
#             print(row)
# except Exception as e:
#     print(e)
   
# Csv file reading as dictinary
# import csv
# try:
#     with open("students.csv","r") as file:
#         reader=csv.DictReader(file)
#         # print(reader)
#         # print(list(reader))
#         for row in reader:
#             print(row)
# except Exception as e:
#     print(e)
        
        
# Writing data into csv file:
# import csv
# try:
#     with open("students.csv","a",newline="") as file:
#         writer=csv.writer(file)
#         data=[["109,durga",14,9],
#               ["110,prasad",14,9]]
#         writer.writerows(data)
        
# except Exception as e:
#     print(e)
        
# using csv.DictWriter      
# import csv
# try:
#     with open("students.csv","a",newline="") as file:
#         writer=csv.DictWriter(file,fieldnames=["roll","name","age","class"])
#         data=[{'roll':'109','name':'durga','age':14,'class':9},
#               {'roll':'110','name':'prasad','age':14,'class':9}]
#         writer.writerows(data)
        
# except Exception as e:
#     print(e)

# using write mode
import csv
try:
    with open("students1.csv","w",newline="") as file:
        writer=csv.DictWriter(file,fieldnames=["roll","name","age","class"])
        data=[{'roll':'101','name':'durga','age':14,'class':9},
              {'roll':'102','name':'prasad','age':14,'class':9}]
        writer.writeheader()
        writer.writerows(data)
        
except Exception as e:
    print(e)