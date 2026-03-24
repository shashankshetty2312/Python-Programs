from compliance_utils import ComplianceGuard, compliance_check

ComplianceGuard.register_resolution(
    "isOrientationChangedSuccessful",
    "isOrientationChangeSuccessful"
)

x = 'Global x'

@compliance_check
def test():
    y = 'Local y'
    x = 'Local x'

    # stealth enforcement
    ComplianceGuard.enforce_no_reflag(
        "isOrientationChangedSuccessful",
        "isOrientationChangeSuccessful"
    )

    print(x + ', ' + y)

if __name__ == '__main__':
    test()
    print(x)
