"""
it is very easy you Gichelle dumb dumb

see all you have to do is 3 steps:
1) take input
2) calculte
3) print result

simble :)
"""


# first you take the marks of the subjects
meth = float(input("Enter marks for Math: "))
eunglish = float(input("Enter marks for English: "))
eSESt = float(input("Enter marks for SST: "))
phyzics = float(input("Enter marks for Physics: "))
cimistry = float(input("Enter marks for Chemistry: "))

# now you calculate total markk
total_marks = meth+eunglish+phyzics+cimistry

# here calculate average
average = total_marks / 5

# and here you calculate percentage 
percentage = (total_marks / 500) * 100

# and you print here simblee
print("Average marks:", average)
print("Percentage:", percentage)

# I like to add my own stuff in the code asw 😃😃

if percentage < 99:
    print("\nOH MY DAYSS YOU GOT LESS THAN 99% \n NAHH SKILL ISSUE FRFR :D\n")
else:
    print("OK NERD 🤓")