def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec



@dec1
def while_loop():
    i = 1
    while i <= 5:
        print(i)
        i = i + 1
    print("Done")

    a = 1
    while a <= 10:
        print('*' * a)
        a = a + 1
    print("Done")

    secret_number = 9
    guess_count = 0
    guess_limit = 3

    while guess_count < guess_limit:
        guess = int(input('Guess: '))
        guess_count += 1
        if guess == secret_number:
            print('You Won!')
            break

    else:
        print('Sorry! You failed !!!')

    command = ""
    started = False
    while True:
        command = input("> ").lower()
        if command == "start":
            if started:
                print("Car is already started")
            else:
                started = True
            print("Car started...")
        elif command == "stop":
            if not started:
                print("Car is already stopped")
            else:
                started = False

            print("Car stopped.")
        elif command == "help":
            print("""
    start - to start the car
    stop - to stop the car
    quit - to quit
            """)
        elif command == "quit":
            break
        else:
            print("Sorry i don't understand it.")
while_loop()
