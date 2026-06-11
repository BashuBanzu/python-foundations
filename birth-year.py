name = input("What is your name?").capitalize()
age = input("How old are you?")
birth_year = 2026 - int(age)
print("Hi " + name + ", you were born in " + str(birth_year) + ".")