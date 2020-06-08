
first_char_small = ord("a")
last_char_small = ord("z")
first_char_upper = ord("A")
last_char_upper = ord("Z")
count_of_char = last_char_small - first_char_small + 1


plaintext = input("Zadej text: ")


key = input("Zadej tajné číslo: ")
while not key.isnumeric():
    key = input("Tajné číslo musí být číslo. Zadej jej znovu prosím.: ")

key = int(key)
while(key/count_of_char > 1):
    key = key - count_of_char

result = ""
for char in plaintext:
    if char.isalpha(): 
        if char.islower():
            first_char = first_char_small
            last_char = last_char_small
        else:
            first_char = first_char_upper
            last_char = last_char_upper
        if ord(char) + key > last_char:
            result = result + chr(first_char - 1 + (ord(char) + key) % last_char)
        else:
            result = result + chr(ord(char) + key)
    else:
        result = result+char

print("Půdovní text: ", plaintext)
print("šifrovaný text: ", result)