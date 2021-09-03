# Import
from os import close
from tcpgecko import TCPGecko


# Def
def dump():
    # Crée le fichier binaire
    f = open("dumpshex.hex", "wb")

    # Demande les infos pour le dump
    print("---Dump :---")
    print("Start address :")
    startAddressDump = str(input())
    print("End address :")
    endAddressDump = str(input())
    print("")
    print("The dump will start. Please wait")
    
    # Récupère les valeurs de la ram à l'endroit séléctionné
    dumpValue = tcp.readmem(int(startAddressDump, 16), int(endAddressDump, 16) - int(startAddressDump, 16) +0x4)

    # Écrit les valeurs
    f.write(dumpValue)

    # Ferme le fichier pour sauvegarder les valeurs
    f.close()

    # Indique que ça à marcher
    print("")
    print("Dump finish !")
    print("You can open your file with a hex editor (for example with HxD).")

def clear():
    # Demande les infos pour le clear
    print("---Clear :---")
    print("Start address :")
    startAddressClear = str(input())
    print("End address :")
    endAddressClear = str(input())
    print("")
    print("The clear will start. Please wait")

    # Mettre à 0 les valeurs de la ram à l'endroit séléctionné
    i = int(int(endAddressClear, 16) - int(startAddressClear, 16) +0x4)
    for i in range(i):
        tcp.pokemem(int(startAddressClear, 16) + i, 0x00000000)
        i = i - 4
    
    # Indique que ça à marcher
    print("")
    print("Clear finish !")

def dumpAndClear():  
    # Crée le fichier binaire
    f = open("dumpshex.hex", "wb")

    # Demande les infos pour le dump
    print("---Dump and clear :---")
    print("Start address :")
    startAddress = str(input())
    print("End address :")
    endAddress = str(input())
    print("")
    print("The dump will start. Please wait")
    
    # Récupère les valeurs de la ram à l'endroit séléctionné
    dumpValue = tcp.readmem(int(startAddress, 16), int(endAddress, 16) - int(startAddress, 16) +0x4)

    # Écrit les valeurs
    f.write(dumpValue)

    # Ferme le fichier pour sauvegarder les valeurs
    f.close()

    # Indique que ça à marcher
    print("")
    print("Dump finish !")
    print("You can open your file with a hex editor (for example with HxD).")

    # Commence le clear
    print("")
    print("The clear will start. Please wait")

    # Mettre à 0 les valeurs de la ram à l'endroit séléctionné
    i = int(int(endAddress, 16) - int(startAddress, 16) +0x4)
    for i in range(i):
        tcp.pokemem(int(startAddress, 16) + i, 0x00000000)
        i = i - 4
    
    # Indique que ça à marcher
    print("")
    print("Clear finish !")
    print("")
    print("The dump and the clear are finish !")


# Affiche le message de bienvenue
print("Welcome in Wii U Ram dump and clear by VCoding and nt games.")
print("")

# Enregistre l'ip
print("Enter your IP please :")
ip = str(input())

# Essaye de se connecter à tcpgecko
print("")
print("The application will try to connect, you will be notified when you are connected.")
tcp = TCPGecko(ip)
connected = bool(True)
print("")
print("You are well connected !")

# Propose les choix
print("")
print("")
print("")
while connected == True:
    print("You now have 3 choices :")
    print("1 - Dump : Allows you to download all the values ​​from one address to another in an .hex file")
    print("2 - Clear : Allows you to delete (set to 0) all values ​​from one address to another")
    print("3 - Dump and clear : Allows to dump the values ​​from one address to another, then to clear the values ​​from one address to another")
    print("")
    print("Write the number or the name of the choice.")

    # Enregistre le choice
    choice = str(input())
    print("")

    # Si le choix est dump, sa lance le dump
    if choice == "1":
        dump()
    if choice == "Dump":
        dump()
    if choice == "dump":
        dump()

    # Si le choix est clear, sa lance le clear
    if choice == "2":
        clear()
    if choice == "Clear":
        clear()
    if choice == "clear":
        clear()

    # Si le choix est dump, sa lance le dump
    if choice == "3":
        dumpAndClear()
    if choice == "Dump and clear":
        dumpAndClear()
    if choice == "dump and clear":
        dumpAndClear()

    ## Si la commande n'existe pas ou qu'il y a une erreur
    #else:
    #    print("Error on the choice of the command !")

    # Demande si il veut continuer
    print("")
    print("Do you want to continue ?")
    print("Yes or No")

    # Enregistre le choice
    continueChoice = str(input())
    print("")

    # Si le choix est non
    if continueChoice == "No":
        # Se deconnecte
        tcp.s.close()

        # Ferme le program
        print("You are disconnected. Thanks for using Wii U Ram dump and clear.")
        print("Goodbye...")
        close()
    # Si le choix est non
    if continueChoice == "no":
        # Se deconnecte
        tcp.s.close()

        # Ferme le program
        print("You are disconnected. Thanks for using Wii U Ram dump and clear.")
        print("Goodbye...")
        exit()

    # Sinon la boucle recommence