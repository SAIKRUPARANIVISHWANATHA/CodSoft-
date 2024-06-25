# Define functions for basic functionality
def add_task(tasks, task):
    tasks.append(task)

def view_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def main():
    tasks = []

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main_1_":
    main()