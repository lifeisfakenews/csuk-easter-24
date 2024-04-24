# WORD: BUnnY

egg_types = ["chocolate", "gold", "silver"]
egg_amounts = [0, 0, 0]

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

for i in range(3):
    egg_amounts[i] = inputInt(f"Enter number of {egg_types[i]} eggs per basket: ")

baskets = inputInt("Enter number of baskets: ")

total_eggs = sum(egg_amounts) * baskets

print(total_eggs)