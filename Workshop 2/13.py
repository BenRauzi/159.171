mark = int(input("Enter a mark: "))

grade = "D"
if mark >= 80:
    grade = "A"
elif mark >= 65:
    grade = "B"
elif mark >= 50:
    grade = "C"

print("The grade for a mark of {} is a {}".format(mark, grade))

