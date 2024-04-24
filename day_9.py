# WORD: 3gGs

participants = []

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

for i in range(4):
    participants.append(inputInt(f"Enter time for participant {i+1}: "))

min = min(participants)

if participants.count(min) > 1:
    print("Tie!")
else:
    print(f"Winning time: {min} seconds. Congratulations to the winner!")