message = input("Enter your message : ")
key = int(input("How many characters should we shift (1 - 26)"))
 
# Prepare your secret message
secret_message = ""
 
# Cycle through each character in the message
for char in message:
 
    # If it isn't a letter then keep it as it is in the else below
    if char.isalpha():
 
        # Get the character code and add the shift amount
        char_code = ord(char)
        char_code += key
 
        # If uppercase then compare to uppercase unicodes
        if char.isupper():
 
            # If bigger than Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26
 
            # If smaller than A add 26
            elif char_code < ord('A'):
                char_code += 26
 
        # Do the same for lowercase characters
        else:
            if char_code > ord('z'):
                char_code -= 26
            elif char_code < ord('a'):
                char_code += 26
 
        # Convert from code to letter and add to message
        secret_message += chr(char_code)
 
    # If not a letter leave the character as is
    else:
        secret_message += char
 
print("Encrypted :", secret_message)
 
# To decrypt the only thing that changes is the sign of the key
key = -key
 
orig_message = ""
 
for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key
 
        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            elif char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            elif char_code < ord('a'):
                char_code += 26
 
        orig_message += chr(char_code)
 
    else:
        orig_message += char
 
print("Decrypted :", orig_message)