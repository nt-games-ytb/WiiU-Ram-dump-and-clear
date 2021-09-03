# Import tcpgecko
from tcpgecko import TCPGecko

# Se connecte à tcpgecko
tcp = TCPGecko("")

# Crée le fichier binaire
f = open("dumpshex", "wb")

# Récupère les valeurs de la ram
dumpBuffer = tcp.readmem(0x00000000, 0x00000000-0x00000000)

# Écrit les valeurs
f.write(dumpBuffer)

# Ferme le fichier pour sauvegarder les valeurs
f.close()

# Se deconnecte
tcp.s.close()