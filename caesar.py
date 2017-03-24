import sys

def encrypt(text, rot):
	strEncrypt = ""
	for eachChar in text:
		# pass each character to rotate_character method and get the new character by shifting the character by int values
		newChar = rotate_character(eachChar, rot)
		strEncrypt = strEncrypt + newChar
	return strEncrypt
	
# *****************************************************************************************************************************
# ***** alphabet_position() functions takes a letter (single char) as input and returns its position in the alphabets *********
# *****************************************************************************************************************************
def alphabet_position(letter):
	letter = letter.lower()
	alphabets = "abcdefghijklmnopqrstuvwxyz"
	numPosition = alphabets.index(letter)
	return numPosition

# *****************************************************************************************************************************
# ***** rotate_character() functions takes a letter and integer and returns a character that is shifted by int poistions ******
# *****************************************************************************************************************************
def rotate_character(char, rot):
	if char.isalpha():
		isUpper = char.isupper()	
		numPosition = alphabet_position(char)    # get the index of the given char in the alphabets
		rotTotalIndex = numPosition + rot        # rotate the character index by the rotation number given
		rotCharIndex = rotTotalIndex % 26
		alphabets = "abcdefghijklmnopqrstuvwxyz"
		retChar = alphabets[rotCharIndex]        # get the rotated characted for the given character
		if isUpper:
			retChar = retChar.upper()
	else:
		retChar = char
	return retChar
