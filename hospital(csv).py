"""
Write a function based program to create a CSV file to create Hospital.CSV file to store information 
about all that hospitals across UAE (add at least 10 records for the same)
haspitalid, hospital name, location, license_no
"""


import csv as yoda 

def addingrecord():
    n = int(input("How many Hospitals : "))
    with open ("Hospital.csv","w", newline='') as inspector:
        for i in range(n):
            wobj = yoda.writer(inspector)
            hospitalid = int(input("Enter Hospital ID: "))
            name = input("Enter Hospital name: ")
            location = input("Enter Location: ")
            license_no = float(input("Enter your License : "))
            lst = [hospitalid, name, location, license_no]
            wobj.writerow(lst)
            print("\nDONE\n")
            
            

def display():
    with open('Hospital.csv', 'r') as read:
        read_read=yoda.reader(read)
        for i in read_read:
            print(i)
        read.close()
        
        
        
def search():
    with open("Hospital.csv","rb") as change:
        id = float(input("Enter the license id: "))
        while True:
            try:
                R=[]
                R=yoda.reader(change)
                if id==R[3]:
                    print(R) 
            except EOFError:
                print("\neyall the records have been displayed :)")
                break


while True:
  u_input = input("""
  Choose your option:
  ----------------------
    halaluya : Add a record
    halaluya 2 : Show all the records
    halaluya 3 : s the record
    halaluya quit: Quit the program
  ----------------------
    Enter the response here: """)

  if u_input == "halaluya":
    addingrecord()
  elif u_input == "halaluya 2":
    display()
  elif u_input == "halaluya 3":
    search()
  elif u_input == "halaluya quit":
    print("\nBYEEE :(")
    break
  else:
    print("\nPLEASE check your reply... very bad very bad 😒")
