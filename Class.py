#  ----------------Q#1)--------------

# ---Tuple item in String, Int and Boolean ----------->>


# mytuple = ("Apple","Bzanana", "Kiwi")
# mytuple1 = (1,2,3,4)
# mytuple2  = (True, False)
# print(mytuple)
# print(mytuple1)
# print(mytuple2)


# ----------Q#2)----------------

# mytuple = ('Apple', 5, 'True')
# print(mytuple)


# ----------Q#3)----------------

# mytuple = ('Apple', 'Banana', 'Orange')
# print(mytuple[1])


# ----------Q#4)----------------

# mytuple = ('Apple', 'Banana', 'Orange')
# print(mytuple[-1])


# ----------Q#5)----------------

# mytuple = ("Apple", "Banana", "Cherry", "Orange")
# print(mytuple[1:3])

 
# ----------Q#6)----------------


# mytuple = ("Apple", "Banana", "Cherry", "Orange")
# print(mytuple[1:])



# ----------Q# 7)----------------z


# mytuple = ("Apple", "Banana", "Cherry", "Orange")
# print(mytuple[:3])



# ----------Q# 8)----------------z


# mytuple = ("Apple", "Banana", "Orange", "cherry")
# if "Kiwi" in mytuple :
#     print('Yes')

# else:
#     print("No")
    

    
# ----------Q# 9)-----------Change  the tuple values-----


# x = {'Apple', 'Banana', 'Cherry'}
# y = list(x)
# y[1] = 'Kiwi'
# x = tuple(y)
# print(x)


# ----------Q# 10)-----------Add the items in tuple----

# mytuple = ("Apple", "Banana", "Cherry")

# y = list(mytuple)
# y.append("Orange")
# mytuple = tuple(y)
# print(mytuple)


#  ----------Q# 11)-----------Remove/Delete items in tuple---------->>>>


# mytuple =  ('Apple', 'Banana', 'Mango')
# y = list(mytuple)
# y.remove('Banana')
# mytuple = tuple(y)
# print(mytuple)


#  ----------Q# 12)-----------Loop through a tuple---------->>>>


# mytuple = ('Apple', 'banana', 'kiwi')
# for x in mytuple:
#     print(x)


#  ----------Q# 13)-----------Loop through index number---------->>>>


# mytuple = ('Apple', 'Banana',  'Mango')
# for x in  range(len(mytuple)):
#     print(mytuple[x])


#  ----------Q# 13)-----------Same program using while loop---------->>>>


mytuple = ('Apple', 'Banana', 'Mango')
i=0
while i < len(mytuple):
    print(mytuple[i])
    i=i+1