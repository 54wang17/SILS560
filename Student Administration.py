__author__ = 'yiqiwang'
# This program is used to simulate student administrate process.
# User can choose to print all students' names and all majors.
# Or new student name and major can be added if they are not in the list.

def main():
    all_students = ['Ellen', 'Sam', 'Victoria', 'Rachel', 'Austin']
    all_majors = ['Information Library Science', 'English', 'Computer Science', 'History', 'Chemistry']
    # call print_instructions() to display instructions to user
    print_instructions()
    user_choice = raw_input("Choose an option: ")
    while user_choice!= '5' :
        if user_choice == '1':
            # get new student name and major
            new_student_name = raw_input("What is the new student's name? ")
            # check if the name of new student has already been in the list
            if new_student_name in all_students:
                print new_student_name,"is already in the list."
                student_index = all_students.index(new_student_name)
                print all_students[student_index]," ",all_majors[student_index]
            # check if the major of new student has already been in the list
            else:
                new_student_major = raw_input("What is the new student's major? ")
                if new_student_major in all_majors:
                    print new_student_major,'is already in the list.'
                # if neither the name nor the major of new student is in the list,add this new student
                else:
                    all_students.append(new_student_name)
                    all_majors.append(new_student_major)
        elif user_choice == '2':
            # print all the students' names in the list
            for student in all_students:
                print student
        elif user_choice == '3':
            # print all the students' majors in the list
            for major in all_majors:
                print major
        elif user_choice == '4':
            #look up a student
            look_up_student = raw_input("Please enter the student name you want to look up: ")
            if look_up_student in all_students:
                student_index = all_students.index(look_up_student)
                print "Student:",all_students[student_index]," Major: ",all_majors[student_index]
            else:
                print "student",look_up_student,"does not exist!"
        else:
            # tell the user that he has entered wrong option
            print "Please enter the right option!"
        # call print_instructions() to display instructions to user
        print_instructions()
        user_choice = raw_input("Choose an option: ")
    print "Done"



def print_instructions():
    print "Please select an action:"
    print "1.Add a student"
    print "2.Print all students"
    print "3.Print all majors"
    print "4.Look up student"
    print "5.Quit"


main()# check if the name of new student has already been in the corresponding list