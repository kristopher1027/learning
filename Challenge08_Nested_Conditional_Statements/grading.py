student_name = "Christopher"
score = 16
attendance = 90
print("===== STUDENT RESULT =====")

if score < 0 or score > 100:
    print("Invalid score.")
else:
    if attendance < 75:
        print("Attendance requirement not met.")
    else:
        if score >= 80:
            
            print("Grade: A")

        elif score >= 70:
            print("Grade: B")
        elif score >= 60:
            print("Grade: C")
        elif score >= 50:
            print("Grade: D")
        else:
            print("Grade: F")
