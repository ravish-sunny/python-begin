def greet_user():
    print ("Hello World")
    name = input ("whats your name?")
    print(f"Nice to meet you, {name}!")
    return name

def calculate_age():
    birth_year = int(input("What year were you born?"))
    current_year = 2025
    age = current_year - birth_year
    return age

def main():
    user_name = greet_user()
    user_age = calculate_age()
    print (f"So, {user_name}, you are about {user_age} years old")
    print ("Thanks for trying my program")

    if __name__ == "_main_":
        main()
    
