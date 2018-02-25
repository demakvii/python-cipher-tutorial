import time, os, sys, transpositionEncrypt,transpositionDecrypt

def main():
    inputFilename = 'hello.txt'

    outputenFilename = 'hello-encrypted.txt'
    outputdecFilename = 'hello-decrypted.txt'
    myKey = 10;
    myMode = input('mode>')
    


    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Exiting...' %(inputFilename))
        sys.exit()

    #if os.path.exists(outputFilename):
    #    print('This will overwrite the file %s, (C)ontinue or  (Q)uit?'%(outputFilename))
    #   respone = input('>')
    #    if not respone.lower().startswith('c'):
    #        sys.exit()


    fileObj =  open(inputFilename)
    content = fileObj.read()
    fileObj.close()


    print('%sing...'%(myMode.title()))

    startTime = time.time()

    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey,content)
    elif myMode == 'decrypt':
        if not os.path.exists(outputenFilename):
             print('The file %s does not exist. Exiting...' %(outputenFilename))
             sys.exit()
        fileObj =  open(outputenFilename)
        content = fileObj.read()
        fileObj.close()
        translated = transpositionDecrypt.decryptMessage(myKey,content)
    totalTime = round(time.time()-startTime,2)
    print('%sion time: %s seconds' % (myMode.title(),totalTime))


    if myMode == 'encrypt':
        outputFileObj = open(outputenFilename,'w')
        outputFileObj.write(translated)
    elif  myMode == 'decrypt':
        outputFileObj = open(outputdecFilename,'w')
        outputFileObj.write(translated)

    outputFileObj.close()

    print('Done %sing %s (%s characters).' %(myMode,inputFilename,len(content)))
    print('%sed file is %s.' %(myMode.title(),outputFileObj))


if __name__ == '__main__':
     main()

        
    
    
    
