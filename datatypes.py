# Numeric data types; integers, floating-point numbers and complex numbers

num1 = 5
print(num1, 'is of type', type(num1))

num2 = 2.0
print(num2, 'is of type', type(num2))

num3 = 1+2j
print(num3, 'is of type', type(num3))

# Python list data type
languages = [ "Swift", "Java", "Python"]

# access element at index 0
print(languages[0]) # Swift

#access element at index 2
print(languages[2]) #Python

# Python tuple data type, once created tuples cannot be modified
product = ('Xbox', 499.99) # product is a tuple with a string value Xbox and integer value 499.99

# Create a tuple
product = ('Microsoft', 'Xbox', 499.99)

# access element at index 0
print(product[0]) # Microsoft

# access ement at index 1
print(product[1]) # Xbox

# python string data type
name = 'Python'
print(name)
message = 'Python for beginners'
print(message)

# python set data type, collection of unique items set is defined by values seperated by commas inside braces{}
#create a set named student_id
student_id = {112, 114,116, 118, 115}

# display student_id elements
print(student_id)

#display type of student_id
print(type(student_id))

