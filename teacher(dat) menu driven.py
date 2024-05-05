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
    with open("Teacher.dat","rb+") as u:
        for i in range(n):
            Teacher_Id = float(input("Enter teacher id: "))
            Teacher_Name = input("Enter the teacher name: ")
            Designation= input("enter the Designation: ")
            print("\nok added\n")
            lst=[Teacher_Id,Teacher_Name,Designation]
        pikol.dump(lst,u)
        print("\nYAY its done now bye :)")


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
                print("\neyall the records have been displayed :)")
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
        print("\nAll the records have been fetched :) ")
        break

#defining UPDATE_record
def UPDATE():
  with open("Teacher.dat","rb+") as superviser_3:
    while True:
      try:
        existing = []
        existing = pikol.load(superviser_3)
        id_to_update = float(input("Enter the id you want to update: "))
        if existing[0]==id_to_update:
          new_id = float(input("Enter the New ID: "))
          new_name = input("Enter the new Name: ")
          new_desig = input("Enter the new Desgination: ")
          
          existing[0]=new_id
          existing[1]=new_name
          existing[2]=new_desig
          
          print("\nDone\n")
          
      except EOFError:
        print("\nAll the records have been fetched :) ")
        break
                    
          
          


while True:
  u_input = input("""
  Choose your option:
  ----------------------
    halaluya : Add a record
    halaluya 2 : Search a record
    halaluya 3 : Show all the records
    halaluya 4 : Update the record
    halaluya quit: Quit the program
  ----------------------
    Enter the response here: """)

  if u_input == "halaluya":
    CREATE()
  elif u_input == "halaluya 2":
    SEARCH()
  elif u_input == "halaluya 3":
    DISPLAY()
  elif u_input == "halaluya 4":
    UPDATE()
  elif u_input == "halaluya quit":
    print("\nBYEEE :(")
    break
  else:
    print("\nPLEASE check your reply... very bad very bad 😒")
