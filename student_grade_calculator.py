def calculate_average(marks):
    return sum(marks) / len(marks)

def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

marks = []

for i in range(5):
    mark = float(input("Enter marks for Subject " + str(i+1) + ": "))
    marks.append(mark)

average = calculate_average(marks)
grade = assign_grade(average)

print("\n----- Result -----")
print("Average Marks =", average)
print("Grade =", grade)