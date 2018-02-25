import pyperclip, detectEnglish, transpositionDecrypt,time

def main():

    myMessage = open('hello-encrypted.txt').read()
    hackedMessage =  hackTransposition(myMessage)
    if hackedMessage == None:
        print('Failed to hack encryption. ')
    else:
       print('Copying hacked message to clipboard:')
       print(hackedMessage)
       pyperclip.copy(hackedMessage)


def hackTransposition(message):
    startTime = time.time()
    print('Decrypting...')
    print('(Press Ctrl-C or Ctrl-D to quit at any time..)')

    for key in range(1,len(message)):
        print('Trying key %s...'%(key))

        decryptedText = transpositionDecrypt.decryptMessage(10,message)
       
        if detectEnglish.isEnglish(decryptedText):
            print()
            endTime = round(time.time()-startTime,3)
            print('Time required for decryption %s seconds' %(endTime))
            print('Possible encryption hack:')
            print('key %s: %s'%(key,decryptedText[:100]))
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('>')
            if response.strip().upper().startswith('D'):
                return decryptedText
    return None

if __name__ == '__main__':
    main()
