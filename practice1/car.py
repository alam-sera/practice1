answer = " "
while answer != "quit":
    answer = input(" ").lower()
    if answer.lower() == "start":
        print("The car has started")
    elif answer == "stop":
        print("The car has stopped")
    elif answer == "help":
        print("""
    start - to start the car
    stop - to stop
    quit - to quit
    """)
    else:
        print("I do not understand that.")
