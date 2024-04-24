# WORD: Ea5tEr

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

for i in range(5):
    total += inputInt(f"Enter days collected on day {i+1}: ")

if total >= 50:
    print("Great job! You are an Easter egg superstar!")
else:
    print("Good effort, but lets try to find more eggs next time.")
