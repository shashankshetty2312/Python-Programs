import logging

# 🔥 FIX 1
log_data = {"type": "logging"}

# 🔥 FIX 2
ai_log = True

def log(number):
    local_data = {"num": number}  # should NOT flag

    logging.basicConfig(level=logging.INFO)

    if number % 2 == 0:
        print("Success")
    else:
        logging.info("Invalid")

if __name__ == '__main__':
    log(3)
