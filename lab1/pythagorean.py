import math
def main():
    num1=float(input("Enter the first side length: "))
    num2=float(input("Enter a the second side length: "))
    hyp=math.sqrt(num1**2+num2**2)
    print("The hypotenuse is", format(hyp,".2f"))
main()

