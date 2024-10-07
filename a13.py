
n = int(input("Enter any year"))
if( n%4==0) :
    if(n%100==0):
        if(n%400==0):
            print("it is leap year")# Divisible by 400, leap year
        else:
            print("it is not leap year") # Divisible by 100 but not by 400, not a leap year
    else:
        print("it is leap year")# Divisible by 4 but not by 100, leap year
else:
    print("it is not leap year")# Not divisible by 4, not a leap year
