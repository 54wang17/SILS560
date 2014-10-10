__author__ = 'yiqiwang'

def main():
    cost = get_user_input()
    print "You bought an item for", format(cost , "d"), "cents and gave me a dollar."
    calculate_correct_amount_of_change(cost)

def get_user_input():
    cost = int(input("Enter price of item (from 25 cents to $1, in 5-cent increments):"))
    if cost == 1:
        cost = 100
    return cost

def calculate_correct_amount_of_change(cost_of_item):
    re = 100-cost_of_item
    quarter_num = re/25
    dime_num = (re-quarter_num*25)/10
    nickel_num = (re-quarter_num*25-dime_num*10)/5
    if quarter_num == 1:
        quarter_output = "quarter, "
    else:
        quarter_output = "quarters, "
    if dime_num == 1:
        dime_output = "dime, "
    else:
        dime_output = "dimes, "
    if nickel_num == 1:
        nickel_output = "nickel."
    else:
        nickel_output = "nickels."
    print "Your change is ",quarter_num, quarter_output,format(dime_num,"d"),dime_output,format(nickel_num,"d"),nickel_output

main()




