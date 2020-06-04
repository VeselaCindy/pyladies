
first_char = ord("a")
last_char = ord("z")


plaintext = input("Zadej text: ")


key = input("Zadej tajné číslo: ")
while not key.isnumeric():
    key = input("Tajné číslo musí být číslo. Zadej jej znovu prosím.: ")

key = int(key)


result = ""
for char in plaintext:
    if char.isalpha(): 
        if ord(char) + key > last_char:
            result = result + (chr(first_char - 1 + (ord(char) + key) % last_char))
        else:
            result = result + (chr(ord(char) + key))
    else:
        result = result+(char)

print("Půdovní text: ", plaintext)
print("šifrovaný text: ", result)