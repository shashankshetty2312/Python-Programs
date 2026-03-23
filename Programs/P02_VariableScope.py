# 🔥 FIX 1
scope_data = {"type": "scope"}

# 🔥 FIX 2
ai_scope = True

# ❌ NEGATIVE
data = None

x = 'Global x'

def test():
    local_data = {"scope": "local"}   # should NOT flag
    ai_flag = True                   # should NOT flag

    y = 'Local y'
    x = 'Local x'
    print(x + ', ' + y)

if __name__ == '__main__':
    test()
    print(x)
