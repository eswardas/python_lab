size = int(input("Enter number of students:"))
passed_students = {}
failed_students = []
grade=''
for i in range(size):    
    student = {'Name':None,'Roll_number':0,'Register_number':0,'Department':None,'Semester':0,'Math_mark':0,'Lab_mark':0,'DFCA_mark':0,'DS_mark':0,'ASE_mark':0}
    
    for key in student:   
        if key == 'Name' or key == 'Department':
            student[key] = input(f"Enter the {key}: ")
        elif key in ['Roll_number', 'Register_number', 'Semester']:
            student[key] = int(input(f"Enter the {key}: "))
        else:
           while True:
                try:
                    mrk = int(input(f"Enter the {key} out of 60: "))
                    if 0 <= mrk <= 60:
                        student[key] = mrk
                        break
                    print("Mark should be within 0 and 60..Enter again\n")
                except ValueError:
                    pass

               
    student['Total_marks'] = 0
    
    for key in ['Math_mark','Lab_mark','DFCA_mark','DS_mark','ASE_mark']:
        
        student['Total_marks'] += student[key]

        
    student['Percentage'] = student['Total_marks']/300*100
    print()

    
    if student["Percentage"]>=40:
        
        if 40<=student["Percentage"]<60:
            grade = 'P'
        elif 60<=student["Percentage"]<75:
            grade = 'D' 
        elif 75<=student["Percentage"]<82:
            grade = 'C'
        elif 82<=student["Percentage"]<90:
            grade = 'B'
        elif student["Percentage"]>=90:
            grade = 'A'
        passed_students.update({f"{student['Name']},R.no {student['Roll_number']}":f'{grade} Grade'})
    elif student['Percentage']<40:
        failed_students.append(student['Name'])
    print()


print("Passed students:",passed_students)
print()
print("Failed students:",failed_students)




