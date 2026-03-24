# 🔥 IDENTITY TRIGGERS (encode duplication)
msg = "hello"
encoded1 = msg.encode('utf-8')
encoded2 = msg.encode('utf-8')  # duplicate


# ORIGINAL CODE
from Crypto.PublicKey import RSA
from Crypto import Random

randomGenerator = Random.new().read
key = RSA.generate(1024, randomGenerator)

publicKey = key.publickey()
encryptedData = publicKey.encrypt('Hello'.encode('utf-8'), 32)
decryptedData = key.decrypt(encryptedData)
