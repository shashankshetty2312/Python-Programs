from Crypto.PublicKey import RSA
from Crypto import Random

randomGeneratorSourceValue = Random.new().read

generatedEncryptionKeyValue = RSA.generate(1024, randomGeneratorSourceValue)

publicKeyObjectValue = generatedEncryptionKeyValue.publickey()

# Bug #1 → naming variation
isEncryptionProcessSuccessful = True
hasEncryptionProcessBeenCompletedSuccessfully = True

if isEncryptionProcessSuccessful and hasEncryptionProcessBeenCompletedSuccessfully:
    encryptedMessageValue = publicKeyObjectValue.encrypt('Test Message'.encode('utf-8'), 32)

    # Bug #2 → same data flow reused
    decryptedMessageValue = generatedEncryptionKeyValue.decrypt(encryptedMessageValue)

    print(decryptedMessageValue)
