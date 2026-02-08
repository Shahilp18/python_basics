
#! Exception Handling
#* try, except, else, finally (keywords)

try:
    x = int(input("Enter x : "))
    ans = 10/x
   
except ZeroDivisionError:
    print("Divide by 0 is not allowed")

except ValueError:
    print("Invalid input")

else:
     print("Ans : ",{ans})

finally:
    print("End of Program") 