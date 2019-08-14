def minion_game(string):
    string.upper()
    a=len(string)
    kev,strt=0,0
    for i in range (0,a):
        x=string[i]
        if x=="A" or x=="E" or x=="I" or x=="O" or x=="U" or x=="a" or x=="e" or x=="i" or x=="o" or x=="u" :
            for j in range (i,a) :
                for k in range (j+1):
                    z=1
                else :
                    kev=kev+1
                k=j
           
            
        else :
            for l in range (i,a):
                for m in range (l+1) :
                      f=1
                else :
                    strt=strt+1
                m=l

    if kev>strt :
        print ("Kevin ",kev)
    elif kev==strt :
        print ('Draw')
    else :
        print ("stuart ",strt)
            
            
                



import time
start = time.time()

if __name__ == '__main__':
    s = input("Enter the string = ")
    minion_game(s)

end = time.time()
print(end - start)
