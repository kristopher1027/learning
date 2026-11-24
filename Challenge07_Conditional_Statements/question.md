# Your challenge: User Access Control System
Difficulty 5/10
Imagine you're developing authentication logic for a backend application.

Your task is to create a program that determines whether a user should be allowed to access a platform.

Start with these variables:
age = 22
is_registered = True
has_valid_id = True



## Requirements
Your program must check the following conditions in order:
1. If the user is below 18, display "Access denied: You must be at least 18 years old."
2. If the user is 18 or older but is not registered, display "Access denied: Please register first."
3. If the user is 18 or older, registered, but has no valid ID, display "Access denied: Valid identification required."
4. Otherwise, display "Access granted: Welcome to the platform!"
Important: Use if, elif, and else. Don't use multiple independent if statements for this challenge.

## Bonus challenge
Test your program with these three scenarios:
Scenario	Age	Registered	Valid ID
A	16	True	True
B	22	False	True
C	25	True	False

Your program should return the appropriate message for each scenario without changing the decision-making logic.