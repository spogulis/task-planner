print("Welcome to your new planning software")

task = {}
master = []
while True:
    title = input("Please enter a task name: ")
    status = input("Was the task done (yes/no)? ")
    status.lower()
    print("Your task was saved in the planner as: \"%s.\"" % title)

    #Create a task dictionary
    if status == "yes":
        task[status] = "Done"
    else:
        task[status] = "Not done"
    new = input("Would you like to enter another task? (yes/no")

    if new == "no":
        break

    #Merge all tasks into a single dictionary

    master.append(task)

for task in master:
    print("Title: %s" % task[title])
