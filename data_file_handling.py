"""Write a menu driven program to Add a record to book.dat file... [b_id,b_name,b_quantity,price] ADD()

Display all records added to "book.dat" SHOW()

Display all records of books whose quantity is more than 10 SEARCH()"""

import pickle as pikol

#defining add_record
def ADD():
  n = int(input("How many users: "))
  with open("book.dat","wb") as u:
    for i in range(n):
      b_id = float(input("Enter the book id: "))
      naam = input("Enter the book name: ")
      b_price= float(input("enter the book price: "))
      b_quantity=int(input("Enter the book quantity: "))
      lst=[b_id,naam,b_price,b_quantity]
      pikol.dump(lst,u)
      print("YAY its done now bye :)")

#defining read_record
def SHOW():
  with open("book.dat","rb") as superviser:
    while True:
      try:
        lst=[]
        lst = pikol.load(superviser)
        print(lst)
      except EOFError:
        print("All the records have been fetched :) ")
        break
    
#defining search_record

def SEARCH():
    with open("book.dat","rb") as superviser_2:
        while True:
            try:
                R=[]
                R=pikol.load(superviser_2)
                if R[3] > 10:
                    print(R)
            except EOFError:
                print("eall the records have been displayed :)")
                break
              
              
while True:
  u_input = input(""" 
  Choose your option: 
  ----------------------
    halaluya : adding 
    halaluya 2 : Showing all records 
    halaluya 3: Showing all records with quantity more than 10  
    halaluya quit: Quit the program
  ----------------------
    Enter the response here: """)

  if u_input == "halaluya":
    ADD()
  elif u_input == "halaluya 2":
    SHOW()
  elif u_input == "halaluya 3":
    SEARCH()
  elif u_input == "halaluya quit":
    print("BYEEE :(")
    break
  else:
    print("PLEASE check your reply... very bad very bad 😒")
  