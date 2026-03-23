import time

# 🔥 FIX 1
time_data = {"type": "stopwatch"}

# 🔥 FIX 2
ai_timer = True

# ❌ NEGATIVE
stuff = None

print("Press Enter to start")

input()
starttime = time.time()

input()
endtime = time.time()

print("Time:", endtime - starttime)
