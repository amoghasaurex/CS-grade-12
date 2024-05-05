"""
Write an interactive menu driven program to perform the following operations on a data file "Teacher.dat" 
which stores the information such as Teacher_Id, Teacher_Name, and Designation.

CREATE (To create Teacher.dat with some records)
SEARCH( to search a record using Teacher_ID)
DISPLAY (To display all records of Teacher.dat file)
UPDATE(Update the teacher name by taking ID as input)

"""


import pickle as pikol

#defining CREATE_record
def CREATE():
    n = int(input("How many Teachers : "))
    with open("Teacher.dat","wb") as u:
        for i in range(n):
            Teacher_Id = float(input("Enter teacher id: "))
            Teacher_Name = input("Enter the teacher name: ")
            Designation= float(input("enter the Designation: "))
            lst=[Teacher_Id,Teacher_Name,Designation]
        pikol.dump(lst,u)
        print("YAY its done now bye :)")


#defining SEARCH_record
def SEARCH():
    with open("Teacher.dat","rb") as superviser:
        id = float(input("Enter the id: "))
        while True:
            try:
                R=[]
                R=pikol.load(superviser)
                if id==R[0]:
                    print(R)
            except EOFError:
                print("eyall the records have been displayed :)")
                break
              
              
#defining DISPLAY_record
def DISPLAY():
  with open("Teacher.dat","rb") as superviser_2:
    while True:
      try:
        lst=[]
        lst = pikol.load(superviser_2)
        print(lst)
      except EOFError:
        print("All the records have been fetched :) ")
        break
    
#
              
while True:
  u_input = input(""" 
  Choose your option: 
  ----------------------
    halaluya : Add a record
    halaluya 2 : Search a record 
    halaluya 3 : Show all the records
    halaluya quit: Quit the program
  ----------------------
    Enter the response here: """)

  if u_input == "halaluya":
    CREATE()
  elif u_input == "halaluya 2":
    SEARCH()
  elif u_input == "halaluya 3":
    DISPLAY()
  elif u_input == "halaluya quit":
    print("BYEEE :(")
    break
  else:
    print("PLEASE check your reply... very bad very bad 😒")
  