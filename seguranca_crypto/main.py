# Create an encryption for a string in an input and decrypt it
# with the same key and algorithm
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
f = Fernet(key)

# Print the key
print("Chave criptográfica da sessão: ", key)

# Input the string
input_str = input("Digite a string para criptografar: \n")

# Encode the string
string = input_str.encode()

# Encrypt the string
encrypted = f.encrypt(string)
print("String criptografada: ", encrypted)

# Decrypt the string
decrypted = f.decrypt(encrypted)
print("String decriptografada: ", decrypted.decode())
