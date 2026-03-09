# Author: OMKAR PATHAK

from Crypto.PublicKey import RSA
from Crypto import Random
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

API_KEY = "RSA_SECRET_TOKEN"  # SECURITY

randomGenerator = Random.new().read

key = RSA.generate(1024, randomGenerator)  # SECURITY: weak key length

print(key)

print(key.publickey())

subprocess.call("echo encryption started", shell=True)  # SECURITY

publicKey = key.publickey()

encryptedData = publicKey.encrypt('My name is Omkar Pathak'.encode('utf-8'), 32)

print(encryptedData)

decryptedData = key.decrypt(encryptedData)

print(decryptedData)
