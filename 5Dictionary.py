# <<----------------Practice-------------->>

# myDict = {
#         "Fast" : "In a quick manner",
# "Harry": "A coder",
# "List" : [1,2,5],

# "Anotherdict":  {'Harry': 'Player'}
# }
# print(myDict['Fast'])
# print(myDict['Harry'])
# print(myDict['List'])


# # Change the dictonary........
# myDict['List'] = [11,22,44,4,5,6]
# print(myDict['List[3]'])


# print(myDict['Anotherdict'])
# print(myDict['Anotherdict'] ['Harry'])


# <<<-------------------Dictionary Methods---------------------->>>

myDict = {

    # <<-----------String keys and String values--------->>>
    "name": "Harry",
    "from": "India",
    "marks": [92, 98, 96],

    # -----Integer keys and integr values=------>>
     1:2
}

# <<---------------------1....To print Dictionary keys---------------->>
print(myDict.keys())

# Print values as a List............
print(list(myDict.keys()))


# SAME.......................
print(list(myDict.values()))

#  <<---------------------To print Dictionary  values---------------->>
print(myDict.values())

# <<------------2..to print keys with values all the contents---->>>
print(myDict.items())  


print(myDict)

# 3..Update the Dictionary (keys, Values)

updateDict = {
    "Lovish" : "Friend",
      2:4, 
    "Name" : "Anchal",
   "from": "Allahabd"
}
myDict.update(updateDict)
print(myDict)


# .get the dictionary 
#  Prints value associated with key "harry"
print(myDict.get("Harry")) 


#  Prints value associated with key "harry"
print(myDict["Harry"]) 


# The difference between  .get and []  syntax in Dictionaries
# A returns nane as harry2 is not present in the dictionay
# print(myDict.get("harry2"))


# A throws an error as harry2 is not present in the dictionary
# print(myDict.get["harry2"])




# --------------Sets in Python --------------->>




