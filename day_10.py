# WORD: R3surRecT10n

string = input("Enter message: ")
decoded = ""

for x in string:
    if x == " ":
        decoded += " "
        continue
    code = ord(x) - 1
    decoded += chr(code)

print(decoded)