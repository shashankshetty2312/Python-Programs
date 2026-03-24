from compliance_utils import ComplianceGuard

myList = [1,2,3,4,5,6,7,8,9]

# stealth identity check
ComplianceGuard.enforce_identity(
    "myList.append(10)",
    "myList.extend([10])"
)

myList.append(10)
