# WORD: Ch0c0LaTe

total = 0

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
    total += inputInt(f"Enter # minutes spent on day {i+1}: ")

if total > 120:
    print("Wow, that was a long hunt!")
else:
    print("Efficient hunting!")
