import csv as yoda

def search():
    with open("Hospital.csv","r") as change:
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

search()