MENUS = (
    "Exit",
    "Load all data",
    "Show all students",
    "Add new student",
    "Remove student",
    "Update student info",
    "Find student by name",
    "Show top N GPA students",
    "Statistics by major",
    "Show students grouped by year",
    "Enroll student to course",
    "Undo last enrollment",
    "Show student courses",
    "Save all data to CSV"
)

menu_selector = dict(enumerate(MENUS))

def show_menu():
    print("========= STUDENT MANAGEMENT =========")
    for k, v in menu_selector.items():
        print(f"{k}. {v}")

if __name__ == "__main__":
    show_menu()
