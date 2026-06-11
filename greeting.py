def get_name():
    name = input("What is your name? ")
    return name

def check_visitor (name):
    try:
        with open("visitors.txt", "r") as file:
            visitors = file.read()
            if name in visitors:
                print("Welcome back," + name + "! Great to see you again!")
            else:
                print("Hello," + name + "! Nice to meet you! First time here!")
    except FileNotFoundError:
        print("Nice to meet you, " + name + "! First time here!")

def save_visitor(name):
    with open("visitors.txt", "a") as file:
        file.write(name + "\n")

name = get_name()
check_visitor(name)
save_visitor(name)