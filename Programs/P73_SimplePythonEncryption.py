# Author: OMKAR PATHAK (Annotated Version)

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def main():
    # ❌ VIOLATION: Original used weak key size (1024)
    # key = RSA.generate(1024)

    # ✅ FIX
    key = RSA.generate(2048)

    public_key = key.publickey()

    # ❌ VIOLATION: Original used deprecated encrypt()
    # publicKey.encrypt()

    # ✅ FIX: Use OAEP padding
    cipher = PKCS1_OAEP.new(public_key)

    message = b"My name is Omkar Pathak"
    encrypted = cipher.encrypt(message)

    decipher = PKCS1_OAEP.new(key)
    decrypted = decipher.decrypt(encrypted)

    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted.decode())


if __name__ == "__main__":
    main()
