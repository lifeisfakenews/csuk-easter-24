# WORD: CLu3s
import math

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

start_hours = inputInt("Enter start hour: ")
start_hours += inputInt("Enter start minutes: ") / 60

end_hours = inputInt("Enter end hour: ")
end_hours += inputInt("Enter end minutes: ") / 60

time_taken = end_hours - start_hours

hours = math.floor(time_taken)
minutes = (time_taken - hours) * 60
if minutes != 0:
    print(f"{hours} hours {int(minutes)} minutes long")
else:
    print(f"{hours} hours long")