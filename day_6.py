# WORD: Ba5k3T

houses = []

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
    houses.append(inputInt(f"Enter # eggs left at house {i+1}: "))

max = max(houses)

if houses.count(max) > 1:
    print("Tie")
else:
    print(f"House {houses.index(max)+1} got the most eggs.")