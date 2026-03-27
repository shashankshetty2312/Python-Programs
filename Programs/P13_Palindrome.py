def palindrome(string):
    revString = string[::-1]          # 🎯 trigger
    
    if string == revString:
        return True                  # 🎯 trigger
    else:
        return False                 # 🎯 trigger


print(palindrome("madam"))           # 🎯 trigger
