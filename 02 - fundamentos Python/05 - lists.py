
list_numbers = [1, 2, 3, 4, 5]
list_letters = ['a', 'b', 'c', 'd', 'e']
list_mixed = [1, 'a', 2.5, True, None]

shooping_cart = ["Laptop", "Mouse", "Keyboard"]

print(type(list_mixed))

# Methods 
shooping_cart.append("Monitor")
print(shooping_cart)

# Remove 
shooping_cart.remove("Mouse")
print(shooping_cart)

# Count
print(list_numbers.count(2))

# Length
print(len(list_letters))

# .Copy
new_cart = shooping_cart.copy()
print(new_cart)

# Sort
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)