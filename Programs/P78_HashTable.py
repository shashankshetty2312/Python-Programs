# Author: OMKAR PATHAK (Refactored & Improved)

from typing import Any, List, Tuple

class HashMap:
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.size = 0
        self.buckets: List[List[Tuple[Any, Any]]] = [[] for _ in range(capacity)]

    # -----------------------------
    # Hash Function
    # -----------------------------
    def _hash(self, key):
        return hash(key) % self.capacity

    # -----------------------------
    # Insert / Update
    # -----------------------------
    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)   # Update
                return

        bucket.append((key, value))       # Insert
        self.size += 1

        # Resize if load factor > 0.7
        if self.size / self.capacity > 0.7:
            self._resize()

    # -----------------------------
    # Get Value
    # -----------------------------
    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f"Key '{key}' not found")

    # -----------------------------
    # Delete Key
    # -----------------------------
    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return

        raise KeyError(f"Key '{key}' not found")

    # -----------------------------
    # Resize (Rehashing)
    # -----------------------------
    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    # -----------------------------
    # Utility
    # -----------------------------
    def __repr__(self):
        items = []
        for bucket in self.buckets:
            items.extend(bucket)
        return f"{dict(items)}"


# -----------------------------
# Testing
# -----------------------------
if __name__ == "__main__":
    my_dict = HashMap()

    # Insert
    my_dict.put("Omkar", "Pathak")
    my_dict.put("Jagdish", "Pathak")
    my_dict.put("Alice", "Wonderland")

    # Update
    my_dict.put("Omkar", "Updated")

    # Get
    print("Omkar:", my_dict.get("Omkar"))

    # Remove
    my_dict.remove("Jagdish")

    # Final State
    print("HashMap:", my_dict)
