import random

def display_intro():
    title = "** A Simple Math Quiz **"
    print("*" * 24)
    print(title)
    print("*" * 24)


def display_menu():
    menu_list = [
        "1. Addition",
        "2. Subtraction",
        "3. Multiplication",
        "4. Integer Division",
        "5. Exit"
    ]
    for item in menu_list:
        print(item)


def display_separator():
    print("-" * 24)


def get_user_input():
    user_input = int(input("Enter your choice: "))
    while not 0 < user_input <= 5:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))
    return user_input


def get_user_solution(problem):
    print("Enter your answer")
    print(problem, end="")
    return int(input(" = "))


def check_solution(user_solution, solution, count):
    if user_solution == solution:
        print("Correct.")
        return count + 1
    print("Incorrect.")
    return count


def menu_option(index, count):
    number_one = random.randrange(1, 21)
    number_two = random.randrange(1, 21)
    options = {
        1: f'{number_one} + {number_two}',
        2: f'{number_one} - {number_two}',
        3: f'{number_one} * {number_two}',
        4: f'{number_one} // {number_two}'
    }
    index = index if index in options else 4
    problem = options[index]
    solution = eval(problem)
    user_solution = get_user_solution(problem)
    count = check_solution(user_solution, solution, count)
    return count


def display_result(total, correct):
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    else:
        percentage = 0
    print(f"You answered {total} questions with {correct} correct.")
    print(f"Your score is {percentage}%. Thank you.")


def main():
    display_intro()
    display_menu()
    display_separator()

    option = get_user_input()
    total = 0
    correct = 0
    while option != 5:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()

    print("Exit the quiz.")
    display_separator()
    display_result(total, correct)

main()
