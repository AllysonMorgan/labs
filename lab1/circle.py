import math
def main():
    radius=input("Enter the radius of a circle: ")
    while True:
        try:
            radius=float(radius)
            break
        except:
            print("Please enter a valid number.")
            radius=input("Enter the radius of a circle: ")
    perimeter=format(2*math.pi*radius,".2f")
    area=format(math.pi*radius**2,".2f")
    message=(f"The circle with radius {radius} has a perimeter of {perimeter} and area of {area}.")
    print(message)
main()
