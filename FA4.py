students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

print ()

class_total = 0

for s in range(1, students + 1):
    print(f"Student {s}")
    student_total = 0
    for sub in range(1, subjects + 1):
        score = float(input(f"Enter score {sub}: "))
        student_total += score
        
    student_avg = student_total / subjects
    print(f"Average for Student {s} = {student_avg}\n")
    
    class_total += student_avg
    
class_avg = class_total / students
print(f"Class Average = {class_avg}")