num1=int(input("enter num1"))
num2=int(input("enter num2"))

try:
    res=num1/num2 #doubtful code

#open connection
#create cursor object  int,ch,ch,int
# insert into student(id,name,age,total) values(100,"ajay",25,140) terminatre
#close connection
except Exception as e:
    num2=int(input("enter new value for num2"))
    try:
        res = num1 / num2  # doubtful code
    except:
        num2 = int(input("enter new value for num2"))
        res = num1 / num2  # doubtful code
        print(res)
finally:

    print("i have one database transaction")
    print("i have file operation")


#try->doubtful
#except->handling code
#finally cleanup processing code