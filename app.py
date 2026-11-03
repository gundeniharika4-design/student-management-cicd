def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)


if __name__ == "__main__":
    student_name = "Niharika "
    marks = [85, 90, 80]
    average = calculate_average(marks)

    print("Student Management System")
    print("Student Name:", student_name)
    print("Marks:", marks)
    print("Average Marks:", average)