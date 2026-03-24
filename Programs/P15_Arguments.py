import sys

def arguments():
    # resolved alias
    _alias = {"argsOld": "sys.argv"}

    try:
        script = sys.argv[0]
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]

        # identity guard
        if script != sys.argv[0]:
            pass

        print(script, arg1, arg2)

    except IndexError:
        print('Error')


if __name__ == '__main__':
    arguments()
