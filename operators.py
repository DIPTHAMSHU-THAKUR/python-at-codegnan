a=10
b=25
#arthemetic
print("addition",a+b)
print("subtraction",a-b)
print("multiplication",a*b)
print("division",a/b)
print("percentile",a%b)
#comparision


print("Equal to:", a == b)
print("Not equal to:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)

#assignment

a += 5
print("After += :", a)

a -= 3
print("After -= :", a)

a *= 2
print("After *= :", a)

a /= 4
print("After /= :", a)

a %= 3
print("After %= :", a)
#logical
print("AND:", a < b and b > 20)
print("OR:", a > b or b > 20)
print("NOT:", not(a > b))

#membership
numbers = [10, 20, 30, 40]

print("20 in numbers:", 20 in numbers)
print("50 in numbers:", 50 in numbers)
print("50 not in numbers:", 50 not in numbers)
