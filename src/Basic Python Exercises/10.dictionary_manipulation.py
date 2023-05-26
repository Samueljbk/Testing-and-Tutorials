# Given a dictionary, write a Python program to create a list of all the keys
# and another list of all the values.

a = {"John": 21, "Mike": 52, "Sarah": 12, "Bob": 45}
keys = []
values = []
for key, value in a.items():
    keys.append(key)
    values.append(value)

print(keys)
print(values)
