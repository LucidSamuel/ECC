from ecies.utils import generate_key
from ecies import encrypt, decrypt
from tkinter import filedialog
import base64, os


secp_k = generate_key()
privhex = secp_k.to_hex()
pubhex = secp_k.public_key.format(True).hex()

# Read the file path of the selected file

filepath = filedialog.askopenfilename()
head, tail = os.path.split(filepath)
newfilepath1 = head + '/encrypted_' + str(tail)
newfilepath2 = head + '/decrypted_' + str(tail)

data = 0
with open(filepath, "rb") as File:
    data = base64.b64encode(File.read())  # convert binary to string data to read file

print("Private_key:",privhex,"\nPublic_key:",pubhex,"Type: ",type(privhex))
print("Binary of the file:", data)
encrypted_secp = encrypt(pubhex,data)
print("Encrypted binary:", encrypted_secp)

with open(newfilepath1,"wb") as EFile:
    EFile.write(base64.b64decode(encrypted_secp))   # To create file with encrypted binary


decrypted_secp = decrypt(privhex, encrypted_secp)
print("\nDecrypted:",decrypted_secp)
with open(newfilepath2,"wb") as DFile:
    DFile.write(base64.b64decode(decrypted_secp)) # convert string to binary to create file using decrypted binary
