student_marks = [78, 92, 85, 60, 74, 88, 95, 67]

sample_list = [0, 1] * 5
print("Repeated sample list:", sample_list)


num_marks = len(student_marks)
print("Number of marks:", num_marks)


print("First mark (positive index):", student_marks[0])
print("Last mark (negative index):", student_marks[-1])


print("First three marks:", student_marks[0:3])
print("Last three marks:", student_marks[-3:])


reversed_marks = student_marks[::-1]
print("Reversed marks:", reversed_marks)


target = 85
for mark in student_marks:
    if mark == target:
        print(f"Found a match: {mark}")


total = 0
for mark in student_marks:
    total += mark
average = total / num_marks
print("Sum of marks:", total)
print("Average mark:", round(average, 2))


smallest = student_marks[0]
largest = student_marks[0]
for mark in student_marks:
    if mark < smallest:
        smallest = mark
    if mark > largest:
        largest = mark

print("Smallest mark:", smallest)
print("Largest mark:", largest)