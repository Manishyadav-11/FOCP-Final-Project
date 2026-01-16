def get_password_length(password):
    count = 0
    for _ in password:
        count = count + 1
    return count


def generate_random_position(password_length):

    import random
    return random.randint(1, password_length)


def get_character_at_position(password, position):
    index = position - 1
    return password[index]


def check_password_character(password, position):
    user_input = input(f"Enter letter at position {position}: ")
    correct_character = get_character_at_position(password, position)
    
    if user_input == correct_character:
        print("Correct")
        return True
    else:
        return False


def main():

    password = input("Enter your password: ")
    
    password_length = get_password_length(password)
    
    if password_length < 9:
        print("Password too short.")
        return
    
    checks_passed = 0
    
    while checks_passed < 3:
        position = generate_random_position(password_length)
        
        if check_password_character(password, position):
            checks_passed = checks_passed + 1
        else:
            print("Security check failed.")
            return
    
    print("Security check passed.")


main()