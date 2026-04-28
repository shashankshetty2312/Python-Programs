x = 'Global x'

def test():
    y = 'Local y'
    local_message = 'Local x'
    print(local_message + ', ' + y)

if __name__ == '__main__':
    test()
    print(x)