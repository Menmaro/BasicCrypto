#Password test
import pickle, shelve

PassFile = open('Passwords.dat', 'wb')

PasswordDict = {'Teacher': 'default',
                'Caesar': 'default',
                'Public': 'default'}

pickle.dump(PasswordDict, PassFile)
PassFile.close()



NewFile = open('Passwords.dat', 'rb')

PasswordDict2 = pickle.load(NewFile)

print(PasswordDict2) 
