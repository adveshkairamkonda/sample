a = 10
b = 5
print("addition : ", a+b)  #output=15
print("subtraction: ", a-b)  # Output: 5
print("multiplication: ", a*b)  # Output: 50
print("division: ", a/b)  # output: 2
print("modulus or reminder: ", a%b)  # Output: 0
print("exponentiation: ", a**b)  #a=10, b=5, it is 10 power 5 which is 10000
print("equal to :", a==b)  # Output: False
print("not equal to ", a!=b)  # Output: True
print("greater than : ", a>b)  # Output: True
print("less than : ", a<b)  # Output: False
print("greater than or equal to : ", a>=b)  # Output: True
print("less than or equal to: ", a<=b)  # Output: False
#and
print("10>3 and 50<20", 10 > 3 and 50 < 20) # Output: False
print("10>3 and 50>20", 10 > 3 and 50 > 20) # Output: True
# or
print("10>3 or 50<20", 10 > 3 or 50 < 20)   # Output: True
print("10>3 or 50>20", 10 > 3 or 50 > 20)   # Output: True
print("10<3 or 50<20", 10 < 3 or 50 < 20)   # Output: False
# not
print("not 3>2 is", not 3 > 2) # not 3>2 not True => False
print("not 3<2 is", not 3 < 2) # not 3<2 not False => True
a+=5
b-=5
c=15
d=20
e=25
#a and b is 10 and 5, as we assigned them at staring on the program
c*=5
d/=5
e%=5
print("a += 5 is ", a)
print("b -= 5 is ", b)
print("c *= 5 is ", c)
print("d /= 5 is ", d)
print("e %= 5 is ", e)

#Membership

num_list = [2, 3, 4, 5, 10]
print("5 is available in [2, 3, 4, 5, 10] ? ", 5 in num_list)
print("7 is available in [2, 3, 4, 5, 10] ? ", 7 in num_list)
name = "John Doe"
print("d is available in name ?", "d" in name)
print("D is available in name ?", "D" in name)
print("Joh is available not in name ?", "Joh" not in name)
print("Jho is available not in name ?", "Jho" not in name)

"""Identity
is - Checks the address if both address are same then returns True
"""
# Identity: TO check which location of the memory it stored use id function
print("a memory location is ", id(a))
print("b memory location is ", id(b))
print("c memory location is ", id(c))
