# todo.py

import os

# Function to display the menu
def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Exit")

# Function to view the to-do list
def view_todo_list(todo_list):
    print("\n--- To-Do List ---")
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to add a task to the to-do list
def add_task(todo_list):
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' has been added.")

# Function to remove a task from the to-do list
def remove_task(todo_list):
    view_todo_list(todo_list)
    if todo_list:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed_task = todo_list.pop(task_num - 1)
                print(f"Task '{removed_task}' has been removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main function to run the to-do list application
def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
