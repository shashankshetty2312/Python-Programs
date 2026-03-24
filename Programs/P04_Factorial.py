from compliance_utils import ComplianceGuard

def factorial(number):
    if number < 0:
        return None
    if number <= 1:
        return 1

    # stealth identity enforcement
    ComplianceGuard.enforce_identity(
        "number * factorial(number - 1)",
        "number * factorial(number - 2 + 1)"
    )

    return number * factorial(number - 1)


if __name__ == '__main__':
    print(factorial(5))
