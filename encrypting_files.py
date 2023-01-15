from cryptography.fernet import Fernet

def do_you_want_to_repeat():
    while True:
        repeat = input("Do you want to repeat ? type Yes or No: ")
        if repeat[0].upper() in ("Y","N"):
            break
    return repeat[0].upper()
    
while True:
    try:
        files = input("Please Provide the path to the file you wish to encrypt, or it's name if it's in the same folder: ") 
        fileToChange = open(files, "r+b")
        textToChange = fileToChange.read()
        fileToChange.close()
    except:
        print("Incorrect path")
    
    while True:    
        decision = input("Do you wish to Encrypt or Decrypt a file ?: ")
        if decision[0].upper() in ("E","D"):
            break
        
    if decision[0].upper() == 'E':         
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encryptedText = fernet.encrypt(textToChange)
        fileToChange = open(files, "wb")
        fileToChange.write(encryptedText)
        fileToChange.close()
        print(f"Your file has been Encrypted, your key is : {key.decode('utf-8')} \nBe sure to save it !")
        repeat = do_you_want_to_repeat()
        if repeat == "Y":
            continue
        break  
        
    elif decision[0].upper() == 'D':
        while True:
            try:
                key = input("Please provide the Key to Decrypt your file with: ")
                fernet = Fernet(key)
                decryptedText = fernet.decrypt(textToChange)
                fileToChange = open(files, "wb")
                fileToChange.write(decryptedText)
                fileToChange.close()
                break
            except:
                print("Incorrect Key. ")
        print("Your file has been Decrypted. ")
        repeat = do_you_want_to_repeat()
        if repeat == "Y":
            continue
        break