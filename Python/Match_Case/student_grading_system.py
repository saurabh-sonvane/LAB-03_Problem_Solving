# Create a student grading system that accepts marks from the user and displays the student's grade and performance

marks = int(input("Enter your marks: "))

match marks:

    case m if 90 <= m <= 100:
        print("Grade: A+")
        print("Performance: Outstanding")

    case m if 80 <= m < 90:
        print("Grade: A")
        print("Performance: Excellent")

    case m if 70 <= m < 80:
        print("Grade: B")
        print("Performance: Very Good")

    case m if 60 <= m < 70:
        print("Grade: C")
        print("Performance: Good")

    case m if 40 <= m < 60:
        print("Grade: D")
        print("Performance: Average")

    case m if 0 <= m < 40:
        print("Grade: F")
        print("Performance: Fail")

    case _:
        print("Invalid Marks")