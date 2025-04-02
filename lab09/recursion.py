def product_of_digits(x):
    x=abs(x)
    if x<10:
        return x
    return ((x%10)*product_of_digits(x//10))

def array_to_string(a,index):
    if index==len(a):
        return ""
    if index==len(a)-1:
        return str(a[index])
    else:
        return str(a[index])+","+array_to_string(a,index+1)
    
def log(base,value):
    if not isinstance(base, int) or not isinstance(value, int):
        raise TypeError("Both base and value must be integers!")
    if value <=0 or base<=1:
        raise ValueError("Value must be greater than 0 and base must be greater than 1!")
    if value<base:
        return 0
    return (1+log(base,value//base))

def main():
    print("Testing product of digits:")
    print(f"The product of 234 is {product_of_digits(234)}.")
    print(f"The product of 12 is {product_of_digits(12)}.")
    print(f"The product of -12 is {product_of_digits(-12)}.")
    print("Testing the array to string:")
    print(f"{[1,2,3,4]} as a string is {array_to_string([1,2,3,4],0)}")
    print(f"{[5,2,6,9,3,15,39]} as a string is {array_to_string([5,2,6,9,3,15,39],0)}")
    print("Testing log:")
    print(f"Log 123456 base 10 is {log(10,123456)}")  
    print(f"Log 64 base 2 is {log(2,64)}")
    print(f"Log 64 base 8 is {log(8,64)}")
    print(f"Log 4567 base 10 is {log(10,4567)}")
    print("Trying to do log 1 base 0 will raise an error.")
    #print(log(0,1))  #just commented out the error lines so the program will still run
    print("Trying to use a non-integer will also raise an error.")
    #print(log(10.5,1.7))
main()