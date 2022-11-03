# ---------------------------Read the File---------------------------------


#Use open function to read the content of a file

# f = open('sample.txt', 'r')

# By default the mode is 'r'
# f = open('sample.txt')


# data = f.read()

# Read  only first  5 characters from the file...........
# data = f.read(5)

# print(data)
# f.close()


#<<<<------------...... Other Methods to read the file....------->>>

# f = open('sample.txt')

# # Read only first line........------------>>>>
# data = f.readline()
# print(data)


# # Read only second line........------------>>>>
# data = f.readline()
# print(data)


# Read only third line........------------>>>>
# data = f.readline()
# print(data)


# # Read only fourth line........------------>>>>
# data = f.readline()
# print(data)


# Read only fifth line and so on........------------>>>>
# data = f.readline()
# print(data)

# f.close()








# ---------------------Write the file------------------------------

# This is write the file------------------------

# f = open('another.txt', 'w')
# f.write("Please2  write this to the file")
# f.close()





# This is append the file------------------------


# f = open('another.txt', 'a')
# f.write(" I am appending this file")
# f.close()






# <<------------------WITH Statement ---------------------->>>


# ______________________Read Function______________________________


# with open('another.txt', 'r') as f:
#     a = f.read
#     print(a)


# ______________________Write Function______________________________


# with open('another.txt', 'w') as f:
#     a = f.write("Me")
#     print(a)
