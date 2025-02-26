import math
import os

# A very simple function
def square(number):
    return number ** 2

def main():
    user_input = float(input("Enter a number: "))
    result = square(user_input)
    print(f"The square of {user_input} is: {result}")

    # A simple loop
    print("Let's compare with math.pow")
    for i in range(10):
        print(f"The square of {i} is:\
              {math.pow(user_input, 2)}")
    
    # A simple condition
    if os.path.exists("samples"):
        print("The directory 'samples' exists") # TODO
    else:
        print("The directory 'samples' does not exist")

if __name__ == "__main__":
    main()
