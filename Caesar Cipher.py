# Caesar Cipher

import time
MAX_KEY_SIZE = 26

def getMode ():
    while True:
        print ('do you wish to encrypt or decypt a message?')
        mode = input().lower()
        if mode in 'encrypt e decypt d'. split():
            return mode
        else:
            print ('Enter either "encrypt" or "e" or "decrypt" or "d"')


def getMessage ():
    print ('Enter your message: ')
    return input()

def getKey ():
    key = 0
    while True:
        print ('Enter a key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage (mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper ():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26

            elif symbol.islower ():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)

        else:
            translated += symbol
    return translated

def playAgain ():
    print ('Do you want to try again?')
    return input ().lower().startswith ('y')

def lockdown ():
    print ('LOCKDOWN')
    print ('Unknown supect attempting to decrypt secret messages')
    print ('Alerting all security styems')

    #time.sleep(3)
    #print ('Security styems activated')
    #print ('Locating supect...')

    #time.sleep (3)
    #print ('Supect found')
    #print('preparing exploives....')

    #time.sleep (3)
    #print ('setting off explosives in:')

    #time.sleep (2)
    #print ('5')
    #time.sleep (2)
    #print ('4')
    #time.sleep (2)
    #print ('3')
    #time.sleep (2)
    #print ('2')
    #time.sleep (3)
    #print ('1')

    
oldMessages = []
while True:
    mode = getMode()
    message = getMessage()
    key = getKey ()

    if message not in oldMessages:
        print ('Your translated text is:')
        print (getTranslatedMessage (mode, message, key))
        if playAgain():
            oldMessages.append(message)
        else:
            break
    else:
        lockdown()
        break
    
            
