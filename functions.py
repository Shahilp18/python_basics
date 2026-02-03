def hello():
    print("Hello W");

hello()

#! Sum
def sum(a, b):
    return a + b

ans = sum(10, 10)
print("Sum =", ans)

#! Average of 3 nos
def avg(a, b, c):
    return (a + b + c)/3

print(avg(10,10,10))

#! Lambda Function
mul = lambda a, b: a * b
print(mul(5, 5))


#! Factorial of n
n = int(input("Enter a no : "))
fact = 1

for i in range(1, n+1):
    fact = fact * i

print("Factorial of ", n, " is ", fact)