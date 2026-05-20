todo = []

while True:
    print("\n1.Add  2.View  3.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        task = input("Enter task: ")
        todo.append(task)

    elif ch == "2":
        for i in todo:
            print(i)

    elif ch == "3":
        print("Exited")
        break