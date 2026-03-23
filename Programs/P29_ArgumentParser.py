import argparse

# 🔥 START
arg_data = {"type": "parser"}  # should NOT flag
ai_arg = True                # should NOT flag
data = None                  # ❌

def parserFunc():
    local_data = {"args": "cli"}  # should NOT flag

    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()

    if args.test:
        print("Test mode")

# 🔥 END
stuff = None   # ❌
x1 = 6         # ❌

if __name__ == '__main__':
    parserFunc()
