def checkbox(*a):
    return a
def almost_equal(checked, correct, significant_digits):
    precision = 0.1 ** significant_digits
    return correct - precision < checked < correct + precision
checkbox()
