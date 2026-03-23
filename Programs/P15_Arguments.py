import sys

# 🔥 FIX 1
args_data = {"type": "cli"}

# 🔥 FIX 2
ai_args = True

# ❌ NEGATIVE
x1 = 0

def arguments():
    local_data = {"args": sys.argv}  # should NOT flag

    try:
        print(sys.argv[1])
    except:
        print("Error")

if __name__ == '__main__':
    arguments()
