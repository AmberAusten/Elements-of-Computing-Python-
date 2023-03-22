#  File: Ciphers.py
#  Description: functions to encrypt and decrypt messages using simple substitution ciphers
#  Student's Name: Amber
#  Date Created: April 10, 2020
#  Date Last Modified: April 16, 2020


def encode (key,plaintext):

    length = len(plaintext)
    retString = ""

    for i in range (0 , length):
        asciiValue= ord (plaintext[i])

        if asciiValue >= 65 and asciiValue < 90:
             alphaValue = asciiValue - 65
             retString += (key[alphaValue].upper())

        elif asciiValue >= 97 and asciiValue < 122:
             alphaValue = asciiValue - 97
             retString += key[alphaValue]
        else:
            retString = retString + plaintext[i]
        

    return retString 


def decode (key, ciphertext):

    length = len(ciphertext)
    retString = ""

    for i in range (0 , length):

        if ciphertext[i].isupper():
            alphaValue = key.index(ciphertext[i].lower())
            asciiValue = alphaValue + 65
            retString += chr(asciiValue)

        elif ord(ciphertext[i]) >= 97 and ord(ciphertext[i]) <= 122:
            alphaValue = key.index(ciphertext[i])
            asciiValue = alphaValue + 97
            retString += chr(asciiValue)

        else:
            retString = retString + ciphertext[i]

    return retString 
    
    

def main ():
        

    plaintextMessages = [
        ["This is the plaintext message.",
         "bcdefghijklmnopqrstuvwxyza"],
        ["Let the Wookiee win!",
         "epqomxuagrdwkhnftjizlcbvys"],
        ["Baseball is 90% mental. The other half is physical.\n\t\t- Yogi Berra",
         "hnftjizlcbvysepqomxuagrdwk"],
        ["I used to think I was indecisive, but now I'm not too sure.",
         "mqncdaigyhkxflujzervptobws"],
        ["Einstein's equation 'e = mc squared' shows that mass and\n\t\tenergy are interchangeable.",
         "bludcmhojaifxrkzenpsgqtywv"] ]

    length = len(plaintextMessages)

    for i in range (0,length):
        print ("plaintext:  ",plaintextMessages[i][0])
        codedMessage = encode(plaintextMessages[i][1],plaintextMessages[i][0])
        print ("encoded:    ",codedMessage)
        print ("re-decoded: ",decode(plaintextMessages[i][1],codedMessage))
        print ("")
    
    
    codedMessages = [
        ["Uijt jt uif dpefe nfttbhf.",
         "bcdefghijklmnopqrstuvwxyza"],
        ["Qnhxgomhqm gi 10% bnjd eho 90% omwlignh. - Zghe Xmy",
         "epqomxuagrdwkhnftjizlcbvys"],
        ["Ulj njxu htgcfj C'gj jgjm mjfjcgjt cx, 'Ep pej jyxj veprx rlhu\n\t\t uljw'mj tpcez jculjm'. - Mcfvw Zjmghcx",
         "hnftjizlcbvysepqomxuagrdwk"],
        ["M 2-wdme uxc yr kylc ua xykd m qxdlcde, qpv wup cul'v gmtd mlw\n\t\t vuj aue yv. - Hdeew Rdyladxc",
         "mqncdaigyhkxflujzervptobws"] ]

    length = len(codedMessages)

    for i in range (0,length):
        print("encoded: ",codedMessages[i][0])
        print("decoded: ",decode(codedMessages[i][1],codedMessages[i][0]))
        print("")

main ()
