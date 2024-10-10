for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()
#1
#22
#333
#4444
#55555

# pattern 2
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
#1
#12
#123
#1234
#12345

#pattern 3
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()    
#*
#**
#***
#****
#*****

#pattern 3
for i in range(1, 6):
    num = 1
    for j in range(6, 0, -1):
        if j > i:
            print(" * ", end=' ')
    print("")

#*   *   *   *   *  
#*   *   *   *  
#*   *   *  
#*   *  
#*



i=1
while i<=3:
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    print()# new line after each row
    i +=1

    
#*
#**
#***










    
        
        
