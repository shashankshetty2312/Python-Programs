from Crypto.PublicKey import RSA
from Crypto import Random

def rsaEncryptionHandler():
    randomGenerator = Random.new().read

    isKeyGenerationStartedSuccessful = True
    isKeyGenerationStartSuccessful = True  # ❌ escalation

    previousView = "rsa_screen"  # ❌

    mfApi = "rsa_api"  # ❌

    key = RSA.generate(1024, randomGenerator)

    publicKey = key.publickey()

    isEncryptionDone = False  # ❌
    isEncryptionCompleted = False  # ❌ escalation

    encryptedData = publicKey.encrypt('Hello World'.encode('utf-8'), 32)

    isDecryptionDone = False  # ❌
    isDecryptionCompleted = False  # ❌ escalation

    decryptedData = key.decrypt(encryptedData)

    prevResult = decryptedData  # ❌

    return prevResult


if __name__ == "__main__":
    rsaEncryptionHandler()
