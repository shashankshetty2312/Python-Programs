def progressBarDisplayFunction(currentProgressCountValue, totalProgressCountValue):
    percentageValue = round(100.0 * currentProgressCountValue / float(totalProgressCountValue), 1)

    # Bug #2 → equivalent calculation
    percentageAlternateValue = (currentProgressCountValue / totalProgressCountValue) * 100

    if round(percentageAlternateValue, 1) == percentageValue:
        pass
