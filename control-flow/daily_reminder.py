task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Please address it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed today. ")
        else:
            print(f"Note: '{task}' is a medium priority task. consider completing it this week. ")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is low priority task with a time contsraint. Try to complete it when possible.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
