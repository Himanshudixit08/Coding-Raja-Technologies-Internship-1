# Task Manager

## Overview

The Task Manager is a Python-based application designed to help you organize and manage your tasks efficiently. This user-friendly tool allows you to add, remove, mark tasks as completed, and display tasks in a well-structured manner. Follow the detailed guide below to understand and make the most of its features.

## Features

1. **Add a New Task:**
   - Enter the task name, priority (HIGH, MEDIUM, LOW), and an optional due date (DD/MM/YYYY).
   - Tasks are added with a default status of "Pending."

2. **Remove Task:**
   - Specify the task index to remove it from the task list.
   - Invalid indices or non-numeric inputs are handled gracefully.

3. **Mark Tasks as Completed:**
   - Indicate task completion by providing the task index.
   - Completed tasks are labeled and saved for reference.

4. **Display Tasks in Order:**
   - View your tasks in a list with details such as priority, due date, and completion status.
   - Tasks are numbered for easy identification.

5. **Exit:**
   - Safely exit the Task Manager, saving any changes made during the session.

## Getting Started

1. **Run the Program:**
   - Execute `main.py` to launch the Task Manager.
   - Follow the on-screen menu for various task management options.

2. **Add a New Task:**
   - Choose option 1 and provide task details when prompted.
   - Due dates are optional, and you can press Enter for no due date.

3. **Remove Task:**
   - Select option 2, enter the task index, and remove tasks effortlessly.

4. **Mark Tasks as Completed:**
   - Opt for option 3, input the task index, and acknowledge completed tasks.

5. **Display Tasks:**
   - Use option 4 to view tasks along with priority, due date (if any), and completion status.

6. **Exit the Program:**
   - Choose option 5 to exit the Task Manager gracefully.

## Example Usage

```bash
Options:
1. Add a New Task
2. Remove Task
3. Mark tasks as Completed
4. Display Tasks in order
5. Exit

Enter your choice (between 1 and 5): 1
Enter task name: Complete Project
Enter priority (HIGH, MEDIUM, LOW): HIGH
Enter due date (DD/MM/YYYY), press Enter for NO due date: 15/01/2023
Task "Complete Project" added successfully.

...

Enter your choice (between 1 and 5): 4
Tasks:
1. Complete Project - Priority: HIGH, Due Date: 15/01/2023, Status: Pending
2. ...

Enter your choice (between 1 and 5): 5
Exiting. Please wait a moment...
```

## Author

[Himanshu Dixit]

Feel free to provide feedback, report issues, or contribute to the project on GitHub. Your input helps us enhance and improve the Budget Tracker for a better user experience.

For any feedback or queries, you can also reach out via email: himanshudixit2002@gmail.com.

Thank you for choosing the Budget Tracker for your financial management needs!
