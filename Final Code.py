userInput1 = "" # Cipher Choice
userInput2 = "" # Encrypt or Decrypt
userInput3 = "" # Message
userInput4 = 0 # Offest 

def intro_msg():
    welcome_msg = """ 
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

                    Welcome to The Caesar / Vigenere Cipher!

            > Here you can encode & decode messages in either format.
            > Caesar Cipher Info: https://www.dcode.fr/caesar-cipher
            > Vigenere Cipher Info: https://www.dcode.fr/vigenere-cipher

                            ... Happy Encrypting!
    
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    """

    print(welcome_msg)


def cipherChoice():

    global userInput1
    
    userInput1 = input("""Which cipher would you like to use? 
    1. Caesar Cipher 
    2. Vigenere Cipher
> """)

    userInput1 = userInput1.lower()      

    if userInput1 != '1' and userInput1 != '2' and userInput1 != 'caesar'  and userInput1 != 'ceasar' and userInput1 != 'vigenere':
        print("""
Sorry, I didn't understand that, please retry your selection (type "1", "2", "caesar" or "vigenere")""")
        retry()
    else:
        if userInput1 == '1' or userInput1 == 'caesar' or userInput1 == 'ceasar':
            userInput1 = 'caesar'
        elif userInput1 == '2' or userInput1 == 'vigenere' :
            userInput1 = 'vigenere'
        encryptChoice()


def encryptChoice():
    global userInput2

    userInput2 = input("""
Would you like to: 
    1. Encrypt a message 
    2. Decrypt a message
> """)  
    
    userInput2 = userInput2.lower()

    if userInput2 != '1' and userInput2 != '2' and userInput2 != 'encrypt'  and userInput2 != 'decrypt':
        print("""
Sorry, I didn't understand that, please retry your selection (type "1", "2", "encrypt" or/ "decrypt")""")
        retry()
    else:
        if userInput2 == '1':
            userInput2 = 'encrypt'
        elif userInput2 == '2' :
            userInput2 = 'decrypt'
        
        message()


def message():
    global userInput3

    userInput3 = input("""
What is the message? 
> """)

    controller()


def controller():
    global userInput1
    global userInput2
    global userInput3
    global userInput4

    if userInput1 == "caesar":
        userInput4 = input("""
What is the offset number?
> """) 
        userInput4 = int(userInput4)
        caesarCipher(userInput2, userInput3, userInput4)

    else: 
        userInput5 = input("""
What is the key?
>""")
        vigenereCipher(userInput2, userInput3, userInput5)

def retry():
    cipherChoice()


def caesarCipher(choice,userMessage,offset):
    message = userMessage
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

        print("""
Your decrypted Caesar Cipher message is: 
""", decoded)


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

        print("""
Your encrypted Caesar Cipher message is: 
""", coded)

    if choice == "encrypt":
        coder(message,offset)
    
    if choice == "decrypt":
        decoder(message,offset)

    # -- Solving a Caesar Cipher without knowing the shift value (brute force) --
    # Use the below code to run through the code and output the code with varying offsets.

    # offset = 1
    # while offset < 25:
    #     decoder(message, offset)
    #     offset +=1
       

def vigenereCipher(choice,userMessage,key):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def coder(message, keyword):
        
        index = 0
        keyword_phrase = ""
        coded_message = ""

        for char in message:
            
            # Deal with non-alphabet characters
            if char not in alphabet:
                keyword_phrase = keyword_phrase + char
                coded_message = coded_message + char
                continue

            # Add keyword character to keyword_phrase
            keyword_phrase = keyword_phrase + keyword[index]

            # Shift message character by its keyword_phrase character
            charIndex = alphabet.find(char)
            keyIndex = alphabet.find(keyword[index])
            newIndex = charIndex + keyIndex

            if newIndex >= len(alphabet):
                newIndex = newIndex % len(alphabet)

            # Add character to coded message
            letter = alphabet[newIndex]
            coded_message = coded_message + letter

            # Update index
            index += 1
            if index >= len(keyword):
                index = index % len(keyword)

        print("""
Your encrypted Vigenere Cipher message is: 
""", coded_message)

    def decoder(message, keyword):
        index = 0
        keyword_phrase = ""
        decoded_message = ""

        for char in message:
            
            # Deal with non-alphabet characters
            if char not in alphabet:
                keyword_phrase = keyword_phrase + char
                decoded_message = decoded_message + char
                continue

            # Add keyword character to keyword_phrase
            keyword_phrase = keyword_phrase + keyword[index]

            # Unshift message character by its keyword_phrase character
            charIndex = alphabet.find(char)
            keyIndex = alphabet.find(keyword[index])
            newIndex = charIndex - keyIndex

            if newIndex >= len(alphabet):
                newIndex = newIndex % len(alphabet)

            # Add character to decoded message
            letter = alphabet[newIndex]
            decoded_message = decoded_message + letter

            # Update index
            index += 1
            if index >= len(keyword):
                index = index % len(keyword)

        print("""
Your encrypted Vigenere Cipher message is: 
""", decoded_message)


    if choice == "encrypt":
        coder(userMessage,key)
    
    if choice == "decrypt":
        decoder(userMessage,key)


intro_msg()
cipherChoice()
