import argparse
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
import sys
import os

# -----------------------------
# Logger Setup
# -----------------------------
def setup_logger(log_file: str, max_bytes: int, backup_count: int):
    logger = logging.getLogger("InputLogger")
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,
        backupCount=backup_count
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


# -----------------------------
# Optional Basic Encryption
# -----------------------------
def simple_encrypt(text: str, key: int = 3) -> str:
    """Very basic Caesar cipher (for demo only, not secure)"""
    encrypted = ""
    for char in text:
        encrypted += chr((ord(char) + key) % 256)
    return encrypted


# -----------------------------
# Input Logger Class
# -----------------------------
class InputLogger:
    def __init__(self, logger, encrypt=False):
        self.logger = logger
        self.encrypt = encrypt

    def log_input(self, user_input: str):
        if self.encrypt:
            user_input = simple_encrypt(user_input)

        self.logger.info(user_input)

    def run(self):
        print("🔐 Safe Input Logger (User Consent Required)")
        print("Type 'exit' or press Ctrl+C to stop.\n")

        try:
            while True:
                user_input = input("Enter text: ").strip()

                if not user_input:
                    print("⚠ Empty input ignored.")
                    continue

                if user_input.lower() == "exit":
                    print("👋 Exiting logger.")
                    break

                self.log_input(user_input)

        except KeyboardInterrupt:
            print("\n⚠ Interrupted by user. Exiting safely.")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        finally:
            print("✅ Logger shutdown complete.")


# -----------------------------
# Argument Parser
# -----------------------------
def parse_args():
    parser = argparse.ArgumentParser(
        description="Advanced Safe Input Logger"
    )

    parser.add_argument(
        "--file",
        type=str,
        default="input_log.txt",
        help="Log file name"
    )

    parser.add_argument(
        "--max-size",
        type=int,
        default=1024 * 1024,  # 1MB
        help="Max log file size before rotation"
    )

    parser.add_argument(
        "--backup",
        type=int,
        default=3,
        help="Number of backup files"
    )

    parser.add_argument(
        "--encrypt",
        action="store_true",
        help="Enable basic encryption"
    )

    return parser.parse_args()


# -----------------------------
# Main Function
# -----------------------------
def main():
    args = parse_args()

    # Ensure directory exists
    log_dir = os.path.dirname(args.file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = setup_logger(
        log_file=args.file,
        max_bytes=args.max_size,
        backup_count=args.backup
    )

    app = InputLogger(logger, encrypt=args.encrypt)
    app.run()


if __name__ == "__main__":
    main()
