# Question says to use nested loops - even though this is unnessecary
def commonStudents(maths_students, cs_students):
    
    print(f"There are {len(maths_students)} students in the Maths class.") #f-string syntax
    print(f"There are {len(cs_students)} students in the Computer Science class.")

    count = 0
    for math_student in maths_students:
        for cs_student in cs_students:
            if math_student == cs_student:
                count += 1
                print(f"Student: {math_student} is enrolled in both classes")
                break #allows for 2 students of the same name without breaking counting. Also prevents unnessecary comparison
      
    print(f"{count} students are enrolled in Computer Science and Maths ")