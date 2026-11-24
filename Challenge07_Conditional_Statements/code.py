age = 22
is_registered = True
has_valid_id = True

if age < 18:
    print("Access denied: You must be at least 18 years old.")

elif not is_registered:
    print("Access denied: Please register first.")

elif not has_valid_id:
    print("Access denied: Valid identification required.")

else:
    print("Access granted: Welcome to the platform!")