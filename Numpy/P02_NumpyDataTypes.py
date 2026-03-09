# ============================================================
# Author: OMKAR PATHAK
# Topic: NumPy Data Types Demonstration
# ============================================================

"""
NumPy provides a wide range of numerical data types that allow
efficient storage and manipulation of data in arrays.

Below are the commonly used NumPy data types.
"""

# ------------------------------
# NUMPY DATA TYPES
# ------------------------------

# bool_       : Boolean (True or False)
# int_        : Default integer type (same as C long)
# intc        : Same as C int
# intp        : Integer used for indexing
#
# Signed Integers
# int8        : -128 to 127
# int16       : -32768 to 32767
# int32       : -2147483648 to 2147483647
# int64       : -9223372036854775808 to 9223372036854775807
#
# Unsigned Integers
# uint8       : 0 to 255
# uint16      : 0 to 65535
# uint32      : 0 to 4294967295
# uint64      : 0 to 18446744073709551615
#
# Floating Point
# float16     : Half precision (16 bits)
# float32     : Single precision (32 bits)
# float64     : Double precision (64 bits)
#
# Complex Numbers
# complex64   : Two 32-bit floats (real + imaginary)
# complex128  : Two 64-bit floats (real + imaginary)

# ============================================================
# IMPORT NUMPY
# ============================================================

import numpy as np

# ============================================================
# BASIC ARRAY CREATION
# ============================================================

print("Creating a basic NumPy array using arange()")

myArray = np.arange(10)
print("Array:", myArray)
print("Data Type:", myArray.dtype)
print()

# ============================================================
# CONVERTING ARRAY TO DIFFERENT DATA TYPES
# ============================================================

print("Converting array to float32")

float_array = np.array(myArray, dtype=np.float32)
print("Array:", float_array)
print("Data Type:", float_array.dtype)
print()

# ============================================================
# COMPLEX NUMBER ARRAY
# ============================================================

print("Converting array to complex64")

complex_array = np.array(myArray, dtype=np.complex64)
print("Array:", complex_array)
print("Data Type:", complex_array.dtype)
print()

# ============================================================
# BOOLEAN ARRAY
# ============================================================

print("Creating Boolean array")

bool_array = np.array([1, 0, 1, 1, 0], dtype=np.bool_)
print("Array:", bool_array)
print("Data Type:", bool_array.dtype)
print()

# ============================================================
# INTEGER TYPES
# ============================================================

print("Different Integer Types")

int8_array = np.array([10, 20, 30], dtype=np.int8)
int16_array = np.array([1000, 2000, 3000], dtype=np.int16)
int32_array = np.array([100000, 200000, 300000], dtype=np.int32)

print("int8 array:", int8_array, "| dtype:", int8_array.dtype)
print("int16 array:", int16_array, "| dtype:", int16_array.dtype)
print("int32 array:", int32_array, "| dtype:", int32_array.dtype)
print()

# ============================================================
# UNSIGNED INTEGER TYPES
# ============================================================

print("Unsigned Integer Types")

uint8_array = np.array([10, 200, 255], dtype=np.uint8)
uint16_array = np.array([1000, 5000, 65000], dtype=np.uint16)

print("uint8 array:", uint8_array, "| dtype:", uint8_array.dtype)
print("uint16 array:", uint16_array, "| dtype:", uint16_array.dtype)
print()

# ============================================================
# FLOAT TYPES
# ============================================================

print("Floating Point Types")

float16_array = np.array([1.5, 2.5, 3.5], dtype=np.float16)
float32_array = np.array([1.123456, 2.123456, 3.123456], dtype=np.float32)
float64_array = np.array([1.123456789, 2.123456789, 3.123456789], dtype=np.float64)

print("float16:", float16_array, "| dtype:", float16_array.dtype)
print("float32:", float32_array, "| dtype:", float32_array.dtype)
print("float64:", float64_array, "| dtype:", float64_array.dtype)
print()

# ============================================================
# COMPLEX NUMBER TYPES
# ============================================================

print("Complex Number Arrays")

complex64_array = np.array([1+2j, 3+4j, 5+6j], dtype=np.complex64)
complex128_array = np.array([1+2j, 3+4j, 5+6j], dtype=np.complex128)

print("complex64:", complex64_array, "| dtype:", complex64_array.dtype)
print("complex128:", complex128_array, "| dtype:", complex128_array.dtype)
print()

# ============================================================
# CHANGING DATA TYPE USING astype()
# ============================================================

print("Changing datatype using astype()")

arr = np.arange(5)
print("Original:", arr, "| dtype:", arr.dtype)

new_arr = arr.astype(np.float64)
print("Converted:", new_arr, "| dtype:", new_arr.dtype)

print()

# ============================================================
# CHECK MEMORY SIZE
# ============================================================

print("Memory usage of different data types")

a = np.array([1,2,3], dtype=np.int8)
b = np.array([1,2,3], dtype=np.int64)

print("int8 itemsize:", a.itemsize, "bytes")
print("int64 itemsize:", b.itemsize, "bytes")

# ============================================================
# END OF PROGRAM
# ============================================================

print("\nNumPy Data Type Demonstration Completed")
