#question1
vow = "aeiouAEIOU"
x = str(input("Enter any characeter"))
if(chr == vow):
    print("vowels")
else:
    print("consonent")

# question 2
n=int(input("Enter the number of days the user is sitting:"))
if n<=5:
  print(n)
  print(n*2,"Rs")
elif 6<=n<=10:
  print(n)
  print(n*3,"Rs")
elif 11<=n<=15:
  print(n)
  print(n*4,"Rs")
else:
  print(n)
  print(n*5,"Rs")

#question 3
n = int(input("enter the integer"))
if n%2 == 0:
    if 2>=n<=5:
        print("Not weird")
    elif(n<=20):
        print("Not weird")
    else:
        print(" ")
else:
    print("Weird")
