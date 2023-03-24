def bondPriceCalc(couponRate, ytm, years, faceValue, paymentsperyear):
    couponPayment = faceValue * ((couponRate / 100) / paymentsperyear)
    calcytm = (ytm / 100) / paymentsperyear
    totalPayments = paymentsperyear * years
    presentCouponValue = (couponPayment / calcytm) * (1 - (1 / ((1 + calcytm)**totalPayments)))
    presentFaceValue = faceValue / ((1 + calcytm)**totalPayments)
    return presentCouponValue + presentFaceValue

print(bondPriceCalc(10, 8, 5, 1000, 2))

print(bondPriceCalc(10, 12, 5, 1000, 2))