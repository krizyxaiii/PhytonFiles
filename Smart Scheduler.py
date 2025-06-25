exam_schedule = []


# Number 1

def add_exam():
    name = input("Enter your name: ")
    date = input("Enter the date (MM/DD/YYYY): ")
    time = input("Enter Time (HH:MM): ")
    room = input("Enter Assigned Room: ")
    exam = {"name": name, "date": date, "time": time, "room": room}
    exam_schedule.append(exam)
    print("Exam Schedule Added!\n")


# Number 2

def view_exams():
    if not exam_schedule:
        print("No Exams Are Planned.\n")
        return

    print("Every Exam Planned:")

    for i, exam in enumerate(exam_schedule, 1):
        print(f"Data {i}: {exam['name']} - {exam['date']} at {exam['time']} in room {exam['room']}")

    print()

# Number 3

def edit_exam():
    if not exam_schedule:
        print("No Exams To Edit.\n")
        return

    view_exams()
    try:
        choice = int(input("Enter The Data Number Of The Exam You Want To Edit: "))
        if choice < 1 or choice > len(exam_schedule):
            print("Invalid Data Number.\n")
            return

        exam = exam_schedule[choice - 1]

        print("Leave Blank To Keep Current Value.")
        name = input(f"Enter New Name (Current: {exam['name']}): ") or exam['name']
        date = input(f"Enter New Date (Current (MM/DD/YYYY): {exam['date']}): ") or exam['date']
        time = input(f"Enter New Time (Current (HH:MM): {exam['time']}): ") or exam['time']
        room = input(f"Enter New Room (Current: {exam['room']}): ") or exam['room']

        exam_schedule[choice - 1] = {"name": name, "date": date, "time": time, "room": room}
        print("Exam Updated Successfully!\n")

    except ValueError:
        print("Please Enter A Valid Number.\n")


# NUmber 4
def delete_exam():
    if not exam_schedule:
        print("No Exams To Delete.\n")
        return

    view_exams()
    try:
        choice = int(input("Enter the Data number of the exam you want to delete: "))
        if choice < 1 or choice > len(exam_schedule):
            print("Invalid Data number.\n")
            return

        deleted = exam_schedule.pop(choice - 1)
        print(f"Exam '{deleted['name']}' on {deleted['date']} has been deleted.\n")

    except ValueError:
        print("Please enter a valid number.\n")

def show_menu():
    print("Smart Scheduler Options")
    print("1. Add a new exam")
    print("2. View all exams")
    print("3. Edit an exam entry")
    print("4. Delete an exam entry")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Select an option (1-5): ")
        print()
        if choice == '1':
            add_exam()
        elif choice == '2':
            view_exams()
        elif choice == '3':
            edit_exam()
        elif choice == '4':
            delete_exam()
        elif choice == '5':
            print("Leaving the Smart Scheduler? Bye!")
            break
        else:
            print("Invalid Choice. Please Select A Number From 1 to 5.\n")


if __name__ == "__main__":
    main()