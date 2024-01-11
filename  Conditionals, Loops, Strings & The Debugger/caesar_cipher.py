def encrypt_letter(letter, shift):
    if is_alphabetic(letter) ==  True:
    # if you want to turn the letter in a num we should use ord("")
    # if you want to turm the number into a character we use chr()

        code = ord(letter)

        new_code = code + shift 

        encrypted = chr(new_code)

        return encrypted
    else:
        return " "

def decrypt_letter(letter,shift):

    if is_alphabetic(letter) == True:

        encrypted_old = ord(letter)
        encrypted_code = encrypted_old - shift 

        decrypt_letter = chr(encrypted_code)

        return decrypt_letter
    else:
        return " "

def is_alphabetic(character):
    value = ord(character)
    if value > 64 and value < 91:
        return True
    return False

def encrypt_message(message,shift):
    #ciphertext = ""
    #letter_code_1 = encrypt_letter(message[0],shift)
    #letter_code_2 = encrypt_letter(message[1],shift)
    #letter_code_3 = encrypt_letter(message[2],shift)
    #letter_code_4 = encrypt_letter(message[3],shift)
    #letter_code_5 = encrypt_letter(message[4],shift)
    #ciphertext = ciphertext + letter_code_1 + letter_code_2 + letter_code_3 + letter_code_4 + letter_code_5 
    index = 0
    while index < len(message):
        letter = encrypt_letter(message[index],shift)
        ciphertext = ciphertext + letter
        index = index + 1

    return ciphertext

def main():
    letter = input("Enter a letter:")
    print(encrypt_letter(letter,3))
    print(decrypt_letter(letter,3))
    print(encrypt_message("VARAG",3))



if __name__ == "__main__":
    main()

