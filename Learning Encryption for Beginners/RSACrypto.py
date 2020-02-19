import random, math, keyGenerator, time, sys, pickle
from itertools import combinations
#Public Key Cryptography
BYTE_SIZE = 256

def String_Delay(String):
    for l in String:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.04)

def KeysFromFile(Mode):
    file = open("Keys.dat", 'rb')
    content = pickle.load(file)
    key = content[Mode]
    n, EorD = key
    return  int(n), int(EorD)

def SubMenu():
    print('Would you like to encrypt or decrypt? (e, d)')
    vchoice = input('> ')
    print()
    
    if vchoice.lower() == 'e':
        message = GetMessage()
        Mode = "Private"
        n, e = KeysFromFile(Mode)
        String_Delay("The program reads the keys from the file.")
        print()
        key = n, e
        filename = 'Message.txt'
        EncryptedText = EncryptAndWriteToFile(message, filename, key)
        String_Delay('Encrypted text:')
        print()
        print(EncryptedText)
        print()


    elif vchoice.lower() == 'd':
        filename = 'Message.txt'
        Mode = "Public"
        n, d = KeysFromFile(Mode)
        key = n, d
        DecryptedText = ReadFromFileAndDecrypt(filename, key)
        String_Delay('Decrypted text:')
        print()
        print(DecryptedText)        
        print()


def GetMessage():
    print("Please enter the message:")
    message = input("> ")
    String_Delay("At this point, the program stores the message to encrypt.")
    print()

    return message

def EncryptMessage(key, message):
    EncryptedMessage = []
    MessageBytes = message.encode('ascii')
    String_Delay("The application coverts the letters into its ascii format (numbers), this makes it easier to encrypt as the equation for encryption is 'C = M to the power e modulus n'.")
    print()
    n, e = key

    for i in range(len(MessageBytes)):

        EncryptedMessage.append(pow(MessageBytes[i],e,n)) #The pow function returns the first number to the power of the second number, modulus the third number.

    return EncryptedMessage

def DecryptMessage(EncryptedMessage, MessageLength, key):
    DecryptedMessage = []
    n, d = key
    String_Delay("The application now runs each character through the equation 'M = C to the power d modulus n' to decrypt the message.")
    print()
    string = ''
    for i in range(len(EncryptedMessage)):
        character = chr(pow(EncryptedMessage[i], d, n))
        DecryptedMessage.extend(character)


    
    return ''.join(DecryptedMessage)


def EncryptAndWriteToFile(message, MessageFilename, key):
    n, e = key
    EncryptedChars = EncryptMessage((n, e), message)
    
    for i in range(len(EncryptedChars)):
        string = ','
        EncryptedChars[i] = str(EncryptedChars[i])

    EncryptedContent = string.join(EncryptedChars) #Joins with a comma so that the program can easily seperate them again.
    String_Delay("The application writes the encrypted message to a file, starting with the message length then continuing with the encrypted letters. These are all seperated by underscore signs('_') and commas for the application to deccrypt later on easily.")
    print()
    
    EncryptedContent = '%s_%s' % (len(message), EncryptedContent) #Same concept with the comma joining.
    file = open((MessageFilename), 'w')
    file.write(EncryptedContent)
    file.close()

    return EncryptedContent

def ReadFromFileAndDecrypt(MessageFilename, key):
    n, d = key
    String_Delay("The application opens the file containing the encrypted message, and splits the message from the message length at the underscore sign.")
    print()
    file = open(MessageFilename, 'r')
    content = file.read()
    MessageLength, DecryptedMessage = content.split('_')
    MessageLength = int(MessageLength)
    
    EncryptedChars = []
    String_Delay("It then seperates the encrypted characters at the commas and runs them through a loop of decryption.")
    print()
    for Chars in DecryptedMessage.split(','):
        EncryptedChars.append(int(Chars))
    return DecryptMessage(EncryptedChars, MessageLength, (n, d))

