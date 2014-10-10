__author__ = 'yiqiwang'

ini_price = float(input("What is the starting price per share in dollars? " ))
share = int(input("How many shares do you want to buy? " ))
ini_pay = share*ini_price*1.02
print "The starting value of this stock is"
print share*ini_price

print "You will be charged"
print ini_pay
print "dollars after the commission."

end_price = float(input("What is the ending price per share in dollars? " ))
end_rec = share*end_price*0.98
print "The ending value of this stock is"
print share*end_price

print "and You will receive"
print end_rec
print "dollars after the commission."

profit = end_rec-ini_pay
print "Your profit is"
print profit
print "dollars,for a "
print profit/ini_pay*100
print "percent increase in value"
