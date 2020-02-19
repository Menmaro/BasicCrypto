import random, math, pickle, time, sys
from itertools import combinations

keysize = 1000

def String_Delay(String):
    for l in String:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.04)

#This function generates Prime numbers
def PrimeNoGen():
    print()
    prime = False
    while prime == False:
        num = random.randint(1, keysize)
        for i in range(2, num//2): #Anything above half of num won't divide by n to produce an integer
            if num % i == 0:
                prime = False
                break
            elif num == 2:
                prime = True
                pn = num # I used pn (stands for prime number)
            else:
                prime = True
                pn = num

    return(pn)
    

#This function generates the keys
def KeyGenerator():
    String_Delay("To generate the keys, prime numbers must first be found. The program does this by picking out a random number 'num', then divides num by all the numbers up to the half of num. If a number is divisible by num, that means num is not a prime number.")
    p = PrimeNoGen()
    q = PrimeNoGen()
    String_Delay("2 variables, p and q, store 2 different random prime numbers.")
    print()
    n = p * q
    String_Delay("Another value, n, must hold the product of p and q. This is esential as n makes up half of both the private key, and the public key.")
    print()
    t = (p-1) * (q-1)
    String_Delay("The totient, t, is worked out but multiplying p-1 with q-1. The totient is used to work out the other half of the public and private keys.")
    print()
    while True:
        e = random.randint(1, t)

        if CoPrime([e, t]):
            break
    String_Delay("e, a random number between 1 and t, is picked out.")
    print()
    String_Delay("e must be relatively prime to t. Numbers are relatively prime if their greatest common diviser is 1. This does not mean that e and t are prime numbers.")
    print()    
    d = ModInv(e, t)
    String_Delay("Now d must be found for the private key. This value d, must satisfy the equation 'd * e = 1 modulus t'. To do this, the modular inverse of e and t must be found. This is d.")
    print()
    PublicKey = (n, e)
    String_Delay("The public key consists of n and e, which are ")
    String_Delay(str(PublicKey))
    print()
    PrivateKey = (n, d)
    String_Delay("The private key consists of n and d, which are ")
    String_Delay(str(PrivateKey))
    print()
    String_Delay("The application now saves the keys to a file to be used later on for encryption and decryption.")
    print()
    return (PublicKey, PrivateKey)


#This function is used with the CoPrime function to find the greatest common diviser of a and b.
def gcd(a, b):
    a = abs(a)
    b = abs(b)
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b

    return a


#Will return true if the greatest common diviser of e and t is 1.
def CoPrime(l):
    for i, j in combinations(l, 2):
        if gcd(i, j) != 1:
            return False
    return True

#This function is the Extended Euclidean algorithm and is used with the ModInv function to find the modular inverse of e and t.
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b%a, a)
        return g, x - (b//a) * y, y


def ModInv(a, t):
    if CoPrime([a, t]):
        linearCombination = egcd(a, t)
        return linearCombination[1] % t
    else:
        return 0


#This function writes the keys to a binary file.
def WriteToFile():
    public, private = KeyGenerator()
    KeysDict = {"Public": public,
                "Private": private}
    NewFile = open("Keys.dat", "wb")
    pickle.dump(KeysDict, NewFile)
    NewFile.close()
