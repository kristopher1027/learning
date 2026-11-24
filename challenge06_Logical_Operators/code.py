age = 18
is_registered = True
has_valid_id = True

print(" ===== ACCESS ELIGIBILITY CHECK =====")
print(f"Is the user least 18? {age >= 18}")
print(f"Is the user registered and has valid ID? {is_registered == True and has_valid_id == True}")
print(f"Is the user registered or has valid ID? {is_registered == True or has_valid_id == True}")
print(f"Is the user not registered? {not is_registered}")
print(f"Is the user eligible for access? {age >= 18 and is_registered == True and has_valid_id == True}") 
print("\n")
age = 16
is_registered = True
has_valid_id = False

print(f"Is the user least 18? {age >= 18}")
print(f"Is the user registered and has valid ID? {is_registered == True and has_valid_id == True}")
print(f"Is the user registered or has valid ID? {is_registered == True or has_valid_id == True}")
print(f"Is the user not registered? {not is_registered}")
print(f"Is the user eligible for access? {age >= 18 and is_registered == True and has_valid_id == True}")