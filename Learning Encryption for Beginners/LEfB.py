# Encryption Teaching Resource
import pickle, shelve, RSACrypto, CaesarCipher, re, keyGenerator
MAX_KEY_SIZE = 26


def Menu():
    print("Learning Encryption")
    print("\nPlease select an option:")
    print("1. Begin Program")
    print("2. Teacher Panel")
    print("3. Exit")
    MenuChoice()


def MenuChoice():
    Choice = input("> ")
    if Choice == "1":
        BeginProgram()
    elif Choice == "2":
        Mode = "Teacher"
        Verification(Mode)
    elif Choice == "3":
        pass
    else:
        print("This isn't an option.")
        MenuChoice()

def BeginProgram():
    print("Welcome to Learning Encryption.")
    print("\nPlease select the lesson:")
    print("1. Caesar Cipher.")
    print("2. Public/Private Key.")
    print("3. Return to main menu.")
    BeginProgramChoice()


def BeginProgramChoice():
    Choice = input("> ")
    if Choice == "1":
        Verification("Caesar")
    elif Choice == "2":
        Verification("Public")
    elif Choice == "3":
        Menu()
    else:
        print("This isn't an option.")
        BeginProgramChoice()


def Verification(Mode):
    FileNew = open('Passwords.dat', 'rb')

    Passwords = pickle.load(FileNew)
    
    if Mode == "Teacher":
        if Passwords[Mode] == "default":
            TeacherPanel()  #This makes sure that there is a way to unlock the whole program or different parts to it.
        else:
            print("Please enter the password(Enter m to return to main menu).")
    elif Mode == "Caesar" or Mode == "Public":
        if Mode == "Caesar" and Passwords[Mode] == "default":
            CaesarCipherMenu()
        elif Mode == "Public" and Passwords[Mode] == "default":
            RSAMenu()
        else:    
            print("Please enter the password given to you by your teacher(Enter m to return to main menu).")
 
    while True:
        UserPass = input("> ")
        if UserPass == Passwords[Mode]:
            break
        elif UserPass.lower() == 'm':
            Menu()
        else:
            print("Incorrect, please try again (Enter m to return to main menu).")

    if Mode == "Teacher":
        TeacherPanel()
    elif Mode == "Caesar":
        CaesarCipherMenu()
    elif Mode == "Public":
        RSAMenu()

    FileNew.close()
            
def GetNewPassword():
    print("Please enter the new password.")
    N1Pass = input("> ")
    #This is regular expressions, it makes sure that the password only has characters that are letters and numbers.
    if re.match("^[A-Za-z0-9]*$", N1Pass) and (len(N1Pass) >= 6):
        print("Please enter the new password again.")
        N2Pass = input("> ")

        if N2Pass == N1Pass:
            NewPass = N2Pass
            Correct = True
            Change = True

        else:
            print("Passwords do not match.")
            GetNewPassword()
    
    else:
        print("This password contains characters that aren't allowed")
        GetNewPassword()
        
    return N1Pass

def TeacherPanel():
    print("What would you like to do?")
    print("1. Assign/Change password to Teacher Panel.")
    print("2. Assign/Change password to Caesar Cipher Module.")
    print("3. Assign/Change password to Public Key module.")
    print("4. Return to main menu.")

    Choice = input("> ")
    module = None

    if Choice == "1":
        module = 'Teacher'
    elif Choice == "2":
        module = 'Caesar'
    elif Choice == "3":
        module = 'Public'
    elif Choice == "4":
        Menu()
    else:
        print("Not an option")
        print()
        TeacherPanel()

    FileNew = open('Passwords.dat', 'rb')

    Passwords = pickle.load(FileNew)

    if Passwords[module] == 'default':
        print("No password is set.")
        print("Would you like to assign a new password?(Y/N)")
        choice = input("> ")
        
        if choice.lower() == 'y':
            NewPass = GetNewPassword()
            Change = True
        else:
            print("False")
            Change = False

    else:
        print ("Would you like to change the password?(Y/N)")
        Choice = input("> ")

        if Choice.lower() == "y":
            print("Please enter the old password")
            Correct = False

            while Correct == False:
                OPass = input("> ")
                if OPass == Passwords[module]:
                    NewPass = GetNewPassword()
                    Change = True

                else:
                    print("Incorrect Password.")
                    print("\nPlease input the old password again.")
                    
        elif choice.lower() == "n":
            print("Returning to menu.")
            Menu()
                
                    

    FileNew.close()
    
    if Change == True:
        NewFile = open('Passwords.dat', 'wb')

        Passwords[module] = NewPass
        pickle.dump(Passwords, NewFile)
            

        print(Passwords)
        NewFile.close()

    else:
        print(Passwords)

    Menu()



def EnterPassword(module):
    FileNew = open('Passwords.dat', 'rb')
    Passwords = pickle.load(FileNew)
    validate = Passwords[module]

    FileNew.close()

    return validate



def GetType():
    print("Are you working with a (enter 3 to return to main menu):")
    print("1. text file.")
    print("2. message.")
    choice = input("> ")

    while True:
        if choice == "1":
            Type = 'text'
            break
        elif choice == "2":
            Type = 'message'
            break
        elif choice == "3":
            Type = 'menu'
            break
        else:
            print("This isn't an option")
            GetType()

    return Type

def CaesarCipherMenu():
    Type = GetType()
    if Type == 'text':
        CaesarCipher.CaesarCipherText()

    elif Type == 'message':
        CaesarCipher.CaesarCipherMessage()

    elif Type == 'menu':
        Menu()

    CaesarCipherMenu()



def RSAMenu():
    print("Do you need to generate new keys? (y, n, or enter 3 to return to main menu)")
    choice = input('> ')

    if choice.lower() == 'y':
        keyGenerator.WriteToFile()
        RSACrypto.SubMenu()
    elif choice.lower() == 'n':
        RSACrypto.SubMenu()
    elif choice.lower() == '3':
        Menu()

    RSAMenu()


Menu()

