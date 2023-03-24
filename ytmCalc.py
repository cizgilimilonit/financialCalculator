def annualYieldCalc(couponRate, faceValue, bondPrice, years, paymentsperyear):
    # Calculate the total number of payments over the life of the bond
    totalPayments = years * paymentsperyear

    # Calculate the periodic coupon payment
    couponPayment = (faceValue * (couponRate/100)) / paymentsperyear

    # Calculate the periodic interest rate
    numerator = couponPayment + (faceValue - bondPrice) / totalPayments
    denominator = (faceValue + bondPrice) / 2
    return (numerator / denominator) * paymentsperyear

print(annualYieldCalc(10, 1000, 957.84, 5, 2))