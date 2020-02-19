import re, time, sys
MAX_KEY_SIZE = 26

def String_Delay(String):
    for l in String:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.04)

def GetMode():
    while True:
        print("Do you want to:")
        print("1.Encrypt?")
        print("2.Decrypt?")
        print()

        Choice = int(input("> "))
        if Choice == 1:
            mode = "e"
            break
        elif Choice == 2:
            mode = "d"
            break
        else:
            print("That is not an option")

    return mode


def GetMessage():
    print("Please enter the message. The message must only contain letters of the alphabet and nothing else.")
    message = input("> ")
    if re.match("^[A-Za-z' ']*$", message):    
        print()
        return message
    else:
        print()
        print("The message has values that are not in the alphabet.")
        print()
        GetMessage()


def GetTextFile():
    print("Enter the name of the text file.")
    print()
    message = input("> ")
    return message

def GetKey():
    while True:
        print("Enter the key number between -%s to %s" % (MAX_KEY_SIZE, MAX_KEY_SIZE))
        key = int(input("> "))
        print()
        if (key > -26 and key < MAX_KEY_SIZE and key != 0):
            break
        else:
            print("The key must be between -%s to %s" % (MAX_KEY_SIZE, MAX_KEY_SIZE))

    return key


def CaesarCipherMessage():
    mode = GetMode()
    message = GetMessage()
    if mode == 'e':
        String_Delay("At this point the program is storing the non-enrypted message (also known as plain text) and the key to use.")
    elif mode == 'd':
        String_Delay("At this point the program is storing the encrypted message (also known as cipher text) and the key to use.")
    print()
    key = GetKey()
    if mode == 'd':
        key = -key

    cipher = ''
    KeyString = str(key)
    String_Delay("Now the program is shifting the message letters ")
    String_Delay(KeyString)
    String_Delay(" times accross.")
    print()
    print(message)
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            cipher += chr(num)

        else:
            cipher += symbol        

    if mode == 'e':
        String_Delay("The program now saves the encrypted message (also known as cipher text) to be displayed.")
    elif mode == 'd':
        String_Delay("The program now saves the decrypted message (also known as plain text) to be displayed.")
    print()
    if mode == 'e':
        String_Delay("The cipher text is: ")
        String_Delay(cipher)
    elif mode == 'd':
        String_Delay("The plain text is: ")
        String_Delay(cipher)    
    print()

 

def CaesarCipherText():
    mode = GetMode()
    PText = GetTextFile()
    key = GetKey()
    if mode == 'd':
        key = -key
    textFile = open(PText, 'r')
    if mode == 'e':
        String_Delay("At this point the program is storing the non-enrypted message (also known as plain text) and the key to use.")
    elif mode == 'd':
        String_Delay("At this point the program is storing the encrypted message (also known as cipher text) and the key to use.")

    print()
    cryptText = textFile.read()
    cipher = ''
    print()
    KeyString = str(key)
    String_Delay("Now the program is shifting the message letters ")
    String_Delay(KeyString)
    String_Delay(" times accross.")
    
    for symbol in cryptText:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            cipher += chr(num)

        else:
            cipher += symbol
            
    if mode == 'e':
        String_Delay("The program now saves the encrypted message (also known as cipher text) to the text file.")
    elif mode == 'd':
        String_Delay("The program now saves the decrypted message (also known as plain text) to the text file.")
    print()
    textFile.close()
    textW = open(PText, 'w')
    textW.write(cipher)
    textW.close()
    if mode == 'e':
        String_Delay("Your text file has been encrypted!")
    elif mode == 'd':
        String_Delay("Your text file has been decrypted!") 
    print()
