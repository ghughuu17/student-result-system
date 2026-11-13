
students = []

while True:

    print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    # ADD STUDENT
    if choice == "1":

        print("\n===== ADD STUDENT =====")

        name = input("Enter Student Name: ")
        roll_no = input("Enter Roll Number: ")

        english = int(input("Enter English Marks: "))
        maths = int(input("Enter Maths Marks: "))
        computer = int(input("Enter Computer Marks: "))

        if (0 <= english <= 100 and
            0 <= maths <= 100 and
            0 <= computer <= 100):

            total = english + maths + computer
            percentage = (total / 300) * 100

            if percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            else:
                grade = "Fail"

            student = {
                "name": name,
                "roll_no": roll_no,
                "english": english,
                "maths": maths,
                "computer": computer,
                "total": total,
                "percentage": percentage,
                "grade": grade
            }

            students.append(student)

            print("\nStudent Added Successfully!")

        else:
            print("\nInvalid Marks! Enter marks between 0 and 100.")
    
    # VIEW ALL STUDENTS
    elif choice == "2":

        print("\n===== VIEW ALL STUDENTS =====")

        print("Total Students:", len(students))

        if len(students) == 0:
            print("No Student Records Found!")

        else:
            for student in students:
                print("\nStudent Name:", student["name"])
                print("Roll Number:", student["roll_no"])
                print("English Marks:", student["english"])
                print("Maths Marks:", student["maths"])
                print("Computer Marks:", student["computer"])
                print("Total Marks:", student["total"], "/ 300")
                print("Percentage:", round(student["percentage"], 2), "%")
                print("Grade:", student["grade"])
                print("------------------------------")

        input("\nPress Enter to return to Menu...")



    # SEARCH STUDENT
    elif choice == "3":

        print("\n===== SEARCH STUDENT =====")

        search = input("Enter Student Roll Number: ")

        found = False

        for student in students:

            if student["roll_no"] == search:

                print("\nStudent Found Successfully!")

                print("------------------------------")
                print("Student Name:", student["name"])
                print("Roll Number:", student["roll_no"])
                print("English Marks:", student["english"])
                print("Maths Marks:", student["maths"])
                print("Computer Marks:", student["computer"])
                print("Total Marks:", student["total"], "/ 300")
                print("Percentage:", round(student["percentage"], 2), "%")
                print("Grade:", student["grade"])
                print("------------------------------")

                found = True
                break

        if found == False:
            print("\nStudent Not Found!")

    # EXIT
    elif choice == "4":

        print("\nThank You for Using Student Result Management System!")
        break

    else:
        print("\nInvalid Choice! Please Select 1 to 4.")
st.title("Student Result Management System")
st.write("Website is working!")