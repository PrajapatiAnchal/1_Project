# ---Sets in Python--------->>>>
# In python, sets output are always in ascending oder

# a = {1,22,3,4,5}
   
# # --------------In Python repeitive items is not allowed----------->>
# a = {1,22,3,4,5,5,5,2}
# print(a)

# print(type(a))

# --------Important : This syntax will create an empty dictionary and not an empty set--->>
# a = {}
# print(type(a))


# 
# An empt y can be created using the below syntax:


# A = set()
# A = {11,2,2,3}
# print(type(A))
# A.add(4)
# A.add(22)

# -------Adding a value in a set------>>

# A.add(22)
# A.add(22)
# print(A)

# -------1.....In set, list AND Dictionary are not allowed for add But tuple is allowed------>>
# A.add([22,2,1])
# print(A)

# OR

# A.add((22,2,1,1))
 
#  OR

# A.add({22:33})
# print(A)

# ----------Operations on Sets------------>>

A = set()
A = {11,2,3,1}


# ________1..________Aceess the elements----->>
# print(A)


# -__________2...Prints the length of the set--------->>
# print(len(A))

# _________________3..Remove the elements in Set------->>
# A.remove(2)
# print(A)


# 4...Remove any elements--------------->>


# print(A.pop())
# print(A)


# 5.........Clear the set---------->>>>>>>>>

print(A)
print(A.clear())
print(A)

                    
# 6.........Union Sets-------------->>>>


print(A.union({89,22,1}))
print(A)


# 7...........Intersection set--------------->>

print(A.intersection({1,44}))
print(A)