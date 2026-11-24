# Your challenge
Build a simple login authentication system.

Start with these variables:
email = "christopher@gmail.com"
password = "python123"
account_exists = True
account_active = True



Your program must follow these rules:
1. If the account doesn't exist, display:
   
   Login failed: Account not found.
2. If the account exists, check whether the email is correct.
3. If the email is correct, check whether the password is correct.
4. If the password is correct, check whether the account is active.
5. If all checks pass, display:
   
   Login successful. Welcome Christopher!
6. If any check fails, display the appropriate error message.
Use these expected credentials:
correct_email = "christopher@gmail.com"
correct_password = "python123"



Important: You must use nested if statements. Don't solve the entire problem using only elif.
3. Testing requirements
Test your program with these five scenarios.
Test checklist

Tick each scenario after testing your program.
[ ] Scenario A

Email: christopher@gmail.com · Password: python123

Account exists: true · Active: true

Expected: Login successful


[ ] Scenario B

Email: wrong@gmail.com · Password: python123

Account exists: true · Active: true

Expected: Incorrect email


[ ] Scenario C

Email: christopher@gmail.com · Password: wrong123

Account exists: true · Active: true

Expected: Incorrect password


[ ] Scenario D

Email: christopher@gmail.com · Password: python123

Account exists: false · Active: true

Expected: Account not found


[ ] Scenario E

Email: christopher@gmail.com · Password: python123

Account exists: true · Active: false

Expected: Account inactive


0/5 scenarios tested
0%




4. Questions you must answer
1. What is a nested if statement?
2. Why would we put one if statement inside another?
3. What is indentation, and why does Python require it?
4. What happens if the first condition is false?