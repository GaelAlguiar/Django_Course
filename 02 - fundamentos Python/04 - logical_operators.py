
# And
age = 21
licensed = True

if (age >= 18 and licensed):
    print("You are allowed to drive.")
else:
    print("You are not allowed to drive.")
    

# Or
is_student = False
membership = False

if (is_student or membership):
    print("You can enter the event.")
else:
    print("You cannot enter the event.")
    
    
# Not
is_admin = False

if not is_admin:
    print("Access denied. Admins only.")
    
    
# Short-circuit evaluation
name = False
print(name and name.upper()) 