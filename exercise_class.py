"""
i = 1
while i < 100:
  i += 2
  print(i+i)

print(3>3.0)
print(3+5)

f = 3e308
g = f*f
print(g)

a = 33
b = 2
c= a//b
print(c)


a=0.0
b=0.0
print(a//b)

a=2
b=a
c=a
c=4
a=6
value = input("Please enter a string: ")
print(f"You entered {value} ")

TypeError=sintax error
ValueError
ZeroDivisionError
NameError
Sin
EnvironmentError
EOFError
a=4
b="la lal la"

print("I´ve got %f $ about %s" %(a,b))

import random 
print(random.random())
print(random.randint(1,10))
/t ->tab
"""


name_house=input("Enter your House name: ")
name_cause=input("Enter your cause: ")
total_quantity=input("Enter your quantity: ")
year=input("Enter your year: ")
print("Dear Governor of the Iron Bank," + "Given the current situation that King’s Landing is facing, the House " + name_house + " is asking for your economic services because" + "of the following cause " + name_cause + ". The debt will be reflected on the Economic Chapter .The estimated total quantity is "+total_quantity + " gold coins."+ " The loan will be returned during the {} following years with{}% of bank interest." + "Thus, the money recovered from the bank, once the loan is completely returned, will be {} gold coins." + "\n\n\n" + "I hope the bank to consider this proposal because the House  " + name_house + " always pay his debts." + "\n\n\n" + "Signed: \n\n \tLord Mace Tyrell")

st="This is a string"
counter = 0
for letter in st:
  if letter == "i" :
    counter=counter +1
print("Number of i:",counter)

st2="This is a string,a string is a sequence of letters"
for letter in st2:
  if letter == "a" or letter == "i":
    letter = "x"
print(st2)

#to change the content of the string i use replace method

st3="This is a string,a string is a sequence of letters"
print(st3.replace("o","x"))
st3=st3.replace("o","x")

for counter in range(1,10):
  print(counter, end = " ")
print()
#end= " "print in the same line with an space
for counter in range(1,20,4):
  print(counter, end = " ")
print()

for counter in range(6):
  print(counter, end=" ")

#Nested loops
#for every iteration of the outer loop.the inner loop will be completely repeated
times= 0 
for counter in range(8):
  print()
  print("counter1",counter)
  for counter2 in range(4):
    #this line is executed 32 times
    print("counter2",counter2, end = " ")
    times= times + 1
print(times)
print(counter,end = " ")
print(counter2, end = " ")

#Branching statements 
#break,continue and return
#break(inside a loop it stops it and finish it)

s= "hello how are you"
counter=0
found=False
while(counter < len(s) and not found ):
  if s[counter] == "w":
    print("Found w at position",counter)
    found=True
    #an alternative would be a break
  else:
    counter = counter+1

for count in range(12):
  if count == 6:
    continue 
  print(count,end= " ")
for count in range(12):
  if count == 6:
    break
  print(count,end=" ")

  #arrays:lists and tuples
  #records:dictionaries,objects

  #lists(position matters,)
list1=["Monday","Tuesday","Wed","Thue","Fri","Sat","Sund"]
  print(list1[2])

  list3=[4,3.5,True,"hello",6]
  print(list3[2])