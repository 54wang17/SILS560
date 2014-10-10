__author__ = 'yiqiwang'

def main():
    OneNumber= float(input("Please input one number: "))
    TwoNumber= float(input("Please input another number: "))

    div(OneNumber,TwoNumber)
    add(OneNumber,TwoNumber)
    subtract(OneNumber,TwoNumber)
    multiply(OneNumber,TwoNumber)


def div(OneNumber,TwoNumber):
    quotient=OneNumber/TwoNumber
    return quotient
def add(OneNumber,TwoNumber):
    sum=OneNumber+TwoNumber
    return sum
def subtract(OneNumber,TwoNumber):
    Minus=OneNumber-TwoNumber
    return Minus
def multiply(OneNumber,TwoNumber):
    product=OneNumber*TwoNumber
    return product
def determine_operator(OneNumber,TwoNumber):
    operator=raw_input("choose your operator, '*' for multiply; :")
    if(operator=="＊"):
        multiply(OneNumber,TwoNumber)


main()

#room = 503
#print ('I am staying in room number', format(room,"d"))