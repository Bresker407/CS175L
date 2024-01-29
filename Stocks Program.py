commpur = float(input('Enter commission rate on stock purchase'))
commsale = float(input('Enter commission rate on stock sale'))
sharepur = int(input('Enter the ammount of shares purchased'))
shareprice = float(input('Enter the cost of each share'))
sharesold = int(input('Enter the ammount of shares sold'))
soldprice = float(input('Enter the sell price per share'))

amountPaid = sharepur * shareprice
 
purchCommission = amountPaid * commpur
 
amountReceived = sharesold * soldprice
 
sellCommission = amountReceived * commsale
 
amountLeft = amountReceived - sellCommission - purchCommission - amountPaid
 
print("Alastor paid", amountPaid, "dollars for his stocks")
 
print("His broker was paid", purchCommission, "dollars during the purchase")
 
print("Alastors stocks sold for", amountReceived, "dollars")
 
print("The broker was paid", sellCommission, "dollars during the sale")
 
if amountLeft < 0:
    print("Alastor lost", abs(amountLeft), "dollars")
else:
    print("Alastor made", amountLeft, "dollars")
