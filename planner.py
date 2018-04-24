tasks = []

#Applications options
def print_menu():
    print("Welcome to your planning software")
    print("[1] - List current tasks")
    print("[2] - Add new task")
    print("[3] - Delete all tasks")
    print("[4] - Quit (and write to file)")

#Add one task including title and status
def add_new_task(tasks, task_name, task_status):
    task = {}
    task["Title"] = task_name
    task["Status"] = task_status
    tasks.append(task)

#List all tasks on screen
def list_all_tasks(tasks):
    for task in tasks:
        print("Title: %s" % task["Title"])
        print("Status: %s" % task["Status"])

#Program logic
while True:
    print_menu() #Show options menu
    action = input("Choose an action: ...")
    if action == "2":
        task_name = input("Please enter a task name: ") #User creates task name/description
        task_status = input("Was the task done (yes/no): ") #User enters task status
        add_new_task(tasks, task_name, task_status.lower())

    if action == "1":
        list_all_tasks(tasks)
        break
    if action == "4":
        break

