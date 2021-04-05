message = "Hweco woh tfvkjsmllwumfea! - cgm arva eitfliv er jeysik dmwkszv!"
keyword = "strawberries"
alphabet = "abcdefghijklmnopqrstuvwxyz"

def encoder(message, keyword):
	
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

	print(coded_message)
	return coded_message


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

	print(decoded_message)
	return decoded_message

#decoder(message, keyword)
#encoder(message, keyword)
