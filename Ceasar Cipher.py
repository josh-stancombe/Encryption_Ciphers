message = "Mjqqt ymjwj! Htslwfyzqfyntsx ts ijhwduynsl rd rjxxflj - N'i qtaj yt mjfw dtzw kjjigfhp ts rd htij, uqjfxj xjsi rj f ijhwduyji rjxxflj ns wjyzws. Ymfspx, Otxm."
alphabet = "abcdefghijklmnopqrstuvwxyz"

def decoder(message,offset):
    decoded = ""
    message = message.lower()

    for letter in message:

        if letter not in alphabet:
            decoded = decoded + letter
            continue

        index = 0

        for char in alphabet:
            if letter == char:
                index = alphabet.find(letter) + offset

        if index >= 26:
            index = index % 26

        decoded = decoded + alphabet[index]

    print(decoded)


def coder(message, offset):
    coded = ""
    message = message.lower()

    for letter in message:  

        if letter not in alphabet:
            coded = coded + letter
            continue

        index = 0

        for char in alphabet:
            if letter == char:
                index = alphabet.find(letter) - offset

        coded = coded + alphabet[index]

    print(coded)


# Function calls - Uncomment a function call below to use.
#decoder(message, -5)
#coder(message, 10)


# -- Solving a Caesar Cipher without knowing the shift value (brute force) --
# Use the below code to run through the code and output the code with varying offsets.

# offset = 1
# while offset < 25:
#     decoder(message, offset)
#     offset +=1

    
