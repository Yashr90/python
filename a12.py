n = int(input())
#if(n >= 0):
#    print(n*n)
#    flag = True
#elif(n <= 0):
#    print(n*n*n)
#    flag = False
#elif(n == 0):
#    print("kuch nhi bhai chill...")
if(n == 0):
    print("")
else:
    if(n <= 0):
        print(n*n*n)
        flag = False
    else:
        if(n>=0):
            print(n*n)
            flag = True
