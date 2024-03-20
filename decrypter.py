import os
import pyaes

def decrypt_file(encrypted_filename, key):
    # Abrir o arquivo criptografado
    with open(encrypted_filename, "rb") as file:
        file_data = file.read()

    # Chave para descriptografia
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    # Remover o arquivo criptografado
    os.remove(encrypted_filename)

    # Criar o arquivo descriptografado
    decrypted_filename = encrypted_filename.replace(".ransomwaretroll", "")
    with open(decrypted_filename, "wb") as new_file:
        new_file.write(decrypt_data)

# Nome do arquivo criptografado
file_name = "teste.txt.ransomwaretroll"

# Chave para descriptografia (deve corresponder à chave usada para criptografar)
key = b"testeransomwares"

# Descriptografar o arquivo
decrypt_file(file_name, key)
