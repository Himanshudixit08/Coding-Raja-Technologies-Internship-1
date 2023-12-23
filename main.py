import json
from datetime import datetime, timedelta


# To load files from tasks
def load_tasks():
  try:
    with open('tasks.json', 'r') as file:
      tasks = json.load(file)
  except FileNotFoundError:
    tasks = []
  return tasks


# feature to save tasks to a file
def save_tasks(tasks):
  with open('tasks.json', 'w') as file:
    json.dump(tasks, file, indent=2)


# feature to add a new file
def add_task(tasks, task_name, priority, due_date):
  new_task = {
      'name': task_name,
      'priority': priority,
      'due_date': due_date.strftime('%d/%m/%Y') if due_date else None,
      'completed': False
  }
  tasks.append(new_task)
  save_tasks(tasks)
  print(f'Task "{task_name}" added successfully.')


# Remove a task
def remove_task(tasks, task_index):
  try:
    task_index = int(task_index)
    if 0 <= task_index < len(tasks):
      removed_task = tasks.pop(task_index)
      save_tasks(tasks)
      print(f'Task "{removed_task["name"]}" removed successfully.')
    else:
      print('Invalid task index.')
  except ValueError:
    print('Invalid input. Please enter a valid task index.')


# Marks as mark_completed
def mark_completed(tasks, task_index):
  try:
    task_index = int(task_index)
    if 0 <= task_index < len(tasks):
      tasks[task_index]['completed'] = True
      save_tasks(tasks)
      print(f'Task "{tasks[task_index]["name"]}" marked as completed.')
    else:
      print('Invalid task index.')
  except ValueError:
    print('Invalid input. Please enter a valid task index.')


# Display task in a list
def display_tasks(tasks):
  if tasks:
    print("Tasks:")
    for i, task in enumerate(tasks):
      status = 'Completed' if task['completed'] else 'Pending'
      due_date = f", Due Date: {task['due_date']}" if task['due_date'] else ""
      print(
          f'{i + 1}. {task["name"]} - Priority: {task["priority"]}{due_date}, Status: {status}'
      )
  else:
    print('No tasks found.')


# Main function
def main():
  tasks = load_tasks()

  while True:
    print('\nOptions:')
    print('1. Add a New_Task')
    print('2. Remove Task')
    print('3. Mark tasks as Completed')
    print('4. Display Tasks in order')
    print('5. Exit')

    choice = input('Enter your choice (between 1 and 5): ')

    if choice == '1':
      task_name = input('Enter task name: ')
      priority = input('Enter priority (HIGH, MEDIUM, LOW): ')
      due_date_str = input(
          'Enter due date ((DD/MM/YYYY), press Enter for NO due date): ')
      due_date = datetime.strptime(due_date_str,
                                   '%d/%m/%Y').date() if due_date_str else None
      add_task(tasks, task_name, priority, due_date)

    elif choice == '2':
      task_index = input('Enter task index to remove: ')
      remove_task(tasks, task_index)

    elif choice == '3':
      task_index = input('Enter task index to mark as completed: ')
      mark_completed(tasks, task_index)

    elif choice == '4':
      display_tasks(tasks)

    elif choice == '5':
      print('Exiting. Please wait a movement...')
      break

    else:
      print('Error : Invalid choice. Please choose a number between 1 and 5.')


if __name__ == "__main__":
  main()
