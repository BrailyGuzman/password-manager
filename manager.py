print("[+] Enter A Secret File Name For Your Passwords.")
storage = input("Enter: ")
while 1:
        print("Enter Your Password Below!")
        password = input("[+] Enter: ")
        file = open(storage + '.txt', 'a')
        file.write(password+"\n")
        file.close()
        print("Added Password to File.")
