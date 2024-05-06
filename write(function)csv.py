"""
    writting function in csv
    
"""


import csv as yoda 
def addingrecord():
    with open ("resident.csv","w",newline=" ") as f1:
        wobj = yoda.writer(f1)
        emiratesid = int(input("Enter emirates ID: "))
        name = input("Enter name: ")
        visano = int(input("Enter visa NO:"))
        natio = input("Enter your nationality: ")
        lst = [emiratesid, name, visano, natio]
        wobj.writerow(lst)

addingrecord()


