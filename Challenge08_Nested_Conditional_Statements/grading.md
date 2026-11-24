# Your challenge
You're building a student grading system for a training institution.

Create these variables:
student_name = "Christopher"
score = 75
attendance = 90



## Your program must follow these rules:
Grading rules
Score	Grade
80–100	A
70–79	B
60–69	C
50–59	D
Below 50	F

Attendance requirement: At least 75%.

## Decision logic:
1. First check whether the score is between 0 and 100.
2. If the score is valid, check attendance.
3. If attendance is below 75%, display "Failed: Attendance requirement not met."
4. If  is sufficient, determine the student's grade using nested conditions.
5. If the score is outside 0–100, display "Invalid score."

## Expected output for the provided values
===== STUDENT RESULT =====

Student: Christopher
Score: 75
Attendance: 90%

Grade: B
Status: Passed

==========================


## Bonus challenge
Test your program using these three cases:
Student	Score	Attendance
Christopher	85	90
David	65	60
Michael	120	90

Observe the different outputs.