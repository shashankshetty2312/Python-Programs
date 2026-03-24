# 🔥 Trigger (string formatting identity)
percent = 50
msg1 = f"{percent}% done"
msg2 = f"{percent}% done"  # duplicate


# ORIGINAL CODE
import time
for i in range(3):
    time.sleep(1)
