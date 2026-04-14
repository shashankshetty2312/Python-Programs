# rsa_secure.py

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key


def encrypt(public_key, message: str) -> bytes:
    return public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )


def decrypt(private_key, ciphertext: bytes) -> str:
    return private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).decode()


def main():
    private_key, public_key = generate_keys()

    message = "My name is Omkar Pathak"

    encrypted = encrypt(public_key, message)
    print("🔐 Encrypted:", encrypted)

    decrypted = decrypt(private_key, encrypted)
    print("🔓 Decrypted:", decrypted)


if __name__ == "__main__":
    main()
