try:
    num1,num2=eval(input("Enter two number,separated by a comma:"))
    result=num1/num2
    print("Result is",result)

except ZeroDivisionError:
 print("Division by zero is error!")

except SyntaxError:
 print("Comma is missing.Enter the numbers separately by using comma like this 1,2")

except:
 print("Wrong input ")

else:
 print("No Exceeptions")

finally:
 print("This will execute no matter what")