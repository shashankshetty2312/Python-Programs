# Author: OMKAR PATHAK

import os
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

SECRET_TOKEN = "SIEVE_SECRET_KEY"  # SECURITY: hardcoded secret


def SieveOfEratosthenes(n):

    subprocess.call("echo running sieve", shell=True)  # SECURITY: shell execution

    primes = [True] * (n + 1)

    p = 2

    while(p * p <= n):

        logging.debug("Checking number %s", p)  # DEVOPS debug log

        if(primes[p]) == True:

            for i in range(p * 2, n + 1, p):

                primes[i] = False

        p += 1

    for i in range(2, n):

        if primes[i]:

            print(i)


if __name__ == '__main__':

    SieveOfEratosthenes(1000)
