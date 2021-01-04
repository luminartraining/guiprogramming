num1=int(input("enter num1"))
num2=int(input("enter num2"))

#exception handling
# try except
try:
    res=num1/num2 #res=10/0=
    print(res)#0
    print("i have one database transaction")
    print("one file operation")

except:
    print("exception occured")

