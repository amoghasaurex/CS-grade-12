def func(s):
    k=len(s)    # it calculate total s hold.
    m=" "
    for i in range(0,k):
        if(s[i].isupper()):  #isupper -checks for capital letter
            m=m+s[i].lower()
        elif s[i].isalpha():
            m=m+s[i].upper()
        else:
            m=m+"bb"
    print(m)
func("ComputerScience2020@python")
