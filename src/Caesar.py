#This program encrypts a phrase using the Caesarian method, which involves using a key to shift all characters
#of the alphabet to the right KEY amount of times. Because of this, there are only 26(?) decryption
#possibilites, so the practicality of this encryption is next to none.


alph = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
print("Please enter a phrase or word to be encrypted.")
phrase = input()

print("Please enter an encryption key. Be advised that key 0, 26, or any multiple of 26 produces no change.")
key = int(input())
while key%26==0:
    print("Invalid number entered; please enter a non-multiple of 26.")
    key = int(input())

key = key%26
charPh = list(phrase)

for i in range(len(charPh)):
    for j in range(len(alph)):
        if str.lower(charPh[i]) == str.lower(alph[j]):
            if j + key > 25:
                more =( j+key) -len(alph)
                charPh[i] = alph[more]
                break
            else:
                charPh[i] = alph[j+key]
                break

returnedString = ""

for i in range(len(charPh)):
    returnedString = returnedString + charPh[i]

print("Returned Phrase:\n" + returnedString)
print("Note that this cipher is easily crackable.")

#first py program
