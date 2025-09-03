name = input("Enter Student Name: ")

#list
marks = []
for i in range(5):
    marks = float(input(f"Enter marks for subject {i+1} "))
    marks.append()
    
total = sum(marks)
percentage = total / 5

if (percentage >= 90):
    grade = 'A+'
elif(percentage >= 80):
    grade = 'A'
elif(percentage >= 70):
    grade = 'B'
elif(percentage >= 60):
    grade = 'C'
else:
    grade = 'FAIL'

print("\n -----Result -----")
print("Name: ", name)
print("Total Marks: ", total)
print("percentage: ", percentage)
print("Grade: ", grade)


