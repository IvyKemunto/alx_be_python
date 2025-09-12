# daily_reminder.py
# This script provides a customized daily reminder based on task priority and time sensitivity

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print(f"Reminder: {reminder}")
else:
    if priority == "high":
        reminder += ". Focus on completing it as soon as possible."
    elif priority == "medium":
        reminder += ". Try to complete it when you have time."
    else:  # low priority
        reminder += ". Consider completing it when you have free time."
    
    print(f"Note: {reminder}")
