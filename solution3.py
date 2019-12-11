import collections
val = input("Enter your value: ")
print("Length of the string: ",len(val))

res = len(val.split())

# printing result
print("The number of words in string are : " + str(res))


print("Length of the string without space: ",len(val) - val.count(' '))


print("commonly occurring alphabet occurs: ", collections.Counter(val).most_common(1)[0])