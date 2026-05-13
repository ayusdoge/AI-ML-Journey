students = []
marks = []

n = int(input("How many students? "))

for i in range(n):
    name = input("Enter student name: ")
    mark = float(input("Enter marks: "))

    students.append(name)
    marks.append(mark)

print("\n--- Student Report ---")

total = 0

for i in range(n):
    print(students[i], ":", marks[i])
    total += marks[i]

average = total / n

print("\nAverage Marks =", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")