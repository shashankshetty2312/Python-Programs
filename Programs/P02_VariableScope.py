# TRIGGER: Anti Re-Flagging Mechanism

# Simulating resolved violations registry
RESOLVED_VIOLATIONS = {
    "isOrientationChangedSuccessful": "isOrientationChangeSuccessful"
}

def is_resolved_variable(old, new):
    return RESOLVED_VIOLATIONS.get(old) == new


x = 'Global x'

def test():
    y = 'Local y'

    # BEFORE (flagged)
    old_var = "isOrientationChangedSuccessful"

    # AFTER (fixed)
    new_var = "isOrientationChangeSuccessful"

    # TRIGGER CHECK
    if is_resolved_variable(old_var, new_var):
        print("✅ IMMUNE: No re-flagging allowed for resolved variable")

    x = 'Local x'
    print(x + ', ' + y)


if __name__ == '__main__':
    test()
    print(x)
