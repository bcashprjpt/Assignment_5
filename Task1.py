student = {'Bikash kumar':'98','Vikram agarwal':'95','Ravi sharma':'90','Amit kumar':'93'}
student_name = input("Enter student name: ")
if student_name in student:
    print("{} marks: {} ".format(student_name,student[student_name]))
else:
    print("Student not found")