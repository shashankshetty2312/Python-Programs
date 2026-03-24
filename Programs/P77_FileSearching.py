# 🔥 IDENTITY TRIGGERS (os.listdir duplication)
import os

path = "."
dirs1 = os.listdir(path)
dirs2 = os.listdir(path)  # duplicate


# ORIGINAL CODE
from pathlib import Path

DIRECTORY = '.'
dirs = [name for name in os.listdir(DIRECTORY)]
