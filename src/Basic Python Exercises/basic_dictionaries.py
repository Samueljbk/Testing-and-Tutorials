# Write a Python program that takes a dictionary
# (for example, a = {"John": 21, "Mike": 52, "Sarah": 12, "Bob": 45})
# and prints each key-value pair in the format key: value.

a = {"John": 21, "Mike": 52, "Sarah": 12, "Bob": 45}
for key, value in a.items():
    print(f"{key}: {value}")
