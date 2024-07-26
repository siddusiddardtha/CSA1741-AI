student(john_doe, mr_smith, math101).
student(jane_smith, mrs_jones, eng202).
student(alice_jones, mr_smith, math101).
student(bob_brown, ms_clark, hist303).
student(mary_jane, mr_smith, phys404).
teacher_of_student(Student, SubjectCode, Teacher) :-
    student(Student, Teacher, SubjectCode).
students_of_teacher(Teacher, Students) :-
    findall(Student, student(Student, Teacher, _), Students).
subjects_of_teacher(Teacher, Subjects) :-
    findall(Subject, student(_, Teacher, Subject), SubjectList),
    sort(SubjectList, Subjects).
teachers_of_subject(SubjectCode, Teachers) :-
    findall(Teacher, student(_, Teacher, SubjectCode), TeacherList),
    sort(TeacherList, Teachers).
