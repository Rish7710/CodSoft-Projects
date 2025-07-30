def show_main_menu():
    print("\n--- Your To-Do List Central ---")
    print("What would you like to do today?")
    print("1. See all my tasks")
    print("2. Add a brand new task")
    print("3. Mark a task as done (Hooray!)")
    print("4. Tweak an existing task")
    print("5. Get rid of a task (Bye, bye!)")
    print("6. Close the To-Do List (See you next time!)")

def show_tasks_overview(tasks_list):
    if not tasks_list:
        print("\nLooks like your to-do list is sparkling clean! Nothing to do yet. 🎉")
        return

    print("\n--- Here's What's On Your Plate ---")
    for index, task_item in enumerate(tasks_list):
        # A little checkmark for completed tasks, or a space for pending ones.
        status_icon = "✔️" if task_item['completed'] else " "
        print(f"{index + 1}. [{status_icon}] {task_item['description']}")

def add_new_task(tasks_list):
    
    new_task_description = input("What's the new task you want to add? ").strip()
    if new_task_description:
        tasks_list.append({"description": new_task_description, "completed": False})
        print(f"Awesome! '{new_task_description}' has been added to your list.")
    else:
        print("Oops! A task needs a description. Let's try that again sometime.")

def complete_a_task(tasks_list):
    
    show_tasks_overview(tasks_list) # First, let's see what tasks are available.
    if not tasks_list: # If there are no tasks, nothing to complete!
        return

    try:
        task_number_to_complete = int(input("Which task number did you finish? "))
        # Adjust for 0-based indexing (humans count from 1, computers from 0)
        task_index = task_number_to_complete - 1

        if 0 <= task_index < len(tasks_list):
            if not tasks_list[task_index]['completed']:
                tasks_list[task_index]['completed'] = True
                print(f"Fantastic! '{tasks_list[task_index]['description']}' is now marked as complete. Great job!")
            else:
                print("Hmm, that task was already marked as done. Double victory!")
        else:
            print("That's not a valid task number. Please pick one from the list.")
    except ValueError:
        print("Oops! Please enter a number for the task. Letters won't work here.")

def modify_task_description(tasks_list):
    show_tasks_overview(tasks_list)
    if not tasks_list:
        return

    try:
        task_number_to_update = int(input("Which task number would you like to change? "))
        task_index = task_number_to_update - 1

        if 0 <= task_index < len(tasks_list):
            old_description = tasks_list[task_index]['description']
            new_description = input(f"Enter the new description for '{old_description}': ").strip()
            if new_description:
                tasks_list[task_index]['description'] = new_description
                print(f"Okay, task {task_number_to_update} has been updated to '{new_description}'.")
            else:
                print("The new description can't be empty. Keeping the old one for now.")
        else:
            print("That task number doesn't seem to exist. Please check your list.")
    except ValueError:
        print("Whoops! Please enter a number for the task you want to update.")

def remove_a_task(tasks_list):

    show_tasks_overview(tasks_list)
    if not tasks_list:
        return

    try:
        task_number_to_delete = int(input("Which task number do you want to remove? "))
        task_index = task_number_to_delete - 1

        if 0 <= task_index < len(tasks_list):
            # .pop() removes the item and returns it, so we can tell the user what was removed.
            removed_task = tasks_list.pop(task_index)
            print(f"Poof! Task '{removed_task['description']}' has been removed from your list.")
        else:
            print("Couldn't find a task with that number. Did you type it correctly?")
    except ValueError:
        print("Oops! Please enter a number to delete a task.")

def run_todo_app():
  
    # Our main storage for tasks. Each task is a little dictionary.
    my_tasks = []

    while True: 
        show_main_menu() 
        user_choice = input("Your choice (just type the number): ")

        if user_choice == '1':
            show_tasks_overview(my_tasks)
        elif user_choice == '2':
            add_new_task(my_tasks)
        elif user_choice == '3':
            complete_a_task(my_tasks)
        elif user_choice == '4':
            modify_task_description(my_tasks)
        elif user_choice == '5':
            remove_a_task(my_tasks)
        elif user_choice == '6':
            print("\nThanks for using your To-Do List! Stay productive! 👋")
            break # Exit the loop, ending the program.
        else:
            print("Hmm, that wasn't a valid option. Please choose a number from 1 to 6.")

# This line is like the "start" button for our To-Do List.
# It makes sure the app only runs when you directly open this file.
if __name__ == "__main__":
    run_todo_app()