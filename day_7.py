# WORD: SwE3t5

def inputInt(prompt):
    user_input = ""
    while not isinstance(user_input, int):
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            if user_input <= 0:
                raise Exception("Must be greater than 0")
        except:
            print(f"{user_input} is not a valid.\nPlease enter a whole number greater than 0")
            user_input = ""
    return user_input

total = inputInt("Enter number: ")

for i in range(total):
    print(f"{''.join(['*' for x in range(i+1)])}")