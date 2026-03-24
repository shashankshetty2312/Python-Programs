from compliance_utils import compliance_check

@compliance_check
def pattern1(level):
    for i in range(1, level + 1):
        print('*' * i)
