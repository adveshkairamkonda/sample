"""
Boolean - True or False
IF there is any empy list/tuple/string/dictionaries the result is false
if they have any items it is true
"""

num_list= [10,20,30,40]   #list
num_tuple= (10,20,30,40)  #tuples
name= 'Advesh'  #string- ' " """
gender="male"   #string- ' " """
about = """Advesh Kairamkonda"""   #string- ' " """
my_set= {10,20,30,40}
details= {"name:","advika","age=24"}
empty_list = []
empty_tuple= ()
empty_string=''
empty_set= {10,20,30,40}
empty_details= {"name:","advika","age=24"}

print(bool(num_tuple))
print(bool(num_tuple))
print(bool(num_list))
print(bool(name))
print(bool(gender))
print(bool(about))
print(bool(my_set))
print(bool(details))
print(bool(empty_list))
print(bool(empty_set))
print(bool(empty_details))
print(bool(empty_tuple))
print(bool(empty_string))


"""
If, if else, elif
#concept 1 - IF
if <condition>
    <excute if condition is true>

#concept2 - if else
if <condition>
    <excute if condition is true>
else <condition>  #excutes if condition is false
    <excute if condition is true>
    
    
#concept3 - elif
if <condition>
    <excute if condition is true>
elif<condition>
    <excute if condition is true>
elif<condition>
    <excute if condition is true>
"""


a=8
b=9
c=30
if a%2==0 and a%3==0:
    print(a)
elif b%2==0 and b%3==0:
    print(b)
elif c%2==0 and c%4==0:
    print(c)

else:
    print("all if conditions are false so it executed else ")


if a%2==0:
    print("a is an even number")
else:
    print("a is an odd number")

"""
control statement: for, while

syntax:
for <item> in <iterable object>:
    <statement>

while <condition>:
    <statement>
"""

fruits =["apple", "orage", "kiwi",10,20]
print("all fruits", fruits)
print("1st index value is ", fruits[1])    #output: orange


for item in fruits:
    if type(item) == str:
        print("item is", item)

