print("Thank you for choosing Python Pizza Deliveries!")

#price list
# small = 15
# medium = 20
# large = 25
# pepperoni = 2
# cheese = 1

size = input("What size of pizza do you want? S, M, or L: ") #What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want to add pepperoni? [Y or N]: ") # Do you want to pepperoni? Y or N
extra_cheese = input("Do you want to add extra cheese? [Y or N]: ") #Do you want extra cheese? Y or N


# 🚨 Don't change the code above 👆

# Write your code below this line 👇


# Functions 👇

# Display order summary
def orderSummary():
    print("[+] Order Summary")
    if size == "S" or size == "s":
        print(f"[+] Pizza Size: Small")
    elif size == "M" or size == "m":
        print(f"[+] Pizza Size: Medium")
    elif size == "L" or size == "l":
        print(f"[+] Pizza Size: Large")
    else:
        print(f"[+] It seems you've entered an invalid input. Please enter S, M, or L")

    #this checks if customer added a pepperoni    
    if add_pepperoni == "y" or add_pepperoni == "Y":
        print("[+] Additional Pepperoni: Yes")
    elif add_pepperoni == "N" or add_pepperoni == "n":
        print("[+] Additional Pepperoni: No")
    else:
        print("[+] There seems to be a problem, please check your entries!")
    
    #this checks if a customer added extra cheese
    if extra_cheese == "Y" or extra_cheese == "y":
        print("[+] Additional Cheese: Yes")
    elif extra_cheese == "N" or extra_cheese == "n":
        print("[+] Additional Cheese: No")
    else:
        print("[+] There seems to be a problem, please check your entry!")
    

# Process the logic from the inputs
def processOrder():
        #process the order for small pizza
        if size == "s" or size == "S":
            price = 15
            if add_pepperoni == "Y" or add_pepperoni == "y":
                price = price + 2
                if extra_cheese == "Y" or extra_cheese == "y":
                    price = price + 1
                    print("Expected Result: Price = 18")
                    print(price)
                else:
                    print("Expected Result: Price = 17")
                    print(price)
            elif add_pepperoni == "N" or add_pepperoni == "n":
                if extra_cheese == "Y" or extra_cheese == "y":
                    price = price + 1
                    print("Expected Result: Price = 16")
                    print(price)
                else:
                    print("Expected result: Price = 15")
                    print(price)
        elif size == "m" or size == "M":
            price = 20
            if add_pepperoni == "Y" or add_pepperoni == "y":
                price = price + 3
                if extra_cheese == "Y" or extra_cheese == "y":
                    price = price + 1
                    print("Expected Result: Price = 23")
                    print(price)
                else:
                    print("Expected Result: Price = 22")
                    print(price)
            elif add_pepperoni == "N" or add_pepperoni == "n":
                if extra_cheese == "Y" or extra_cheese == "y":
                    price = price + 1
                    print("Expected Result: Price = 21")
                    print(price)
                else:
                    print("Expected result: Price = 20")
                    print(price)

        elif size == "l" or size == "L":
            price = 25
            if add_pepperoni == "Y" or add_pepperoni == "y":
                price = price + 3
                if extra_cheese == "Y" or extra_cheese == "y":
                    price = price + 1
                    print("Expected Result: Price = 23")
                    print(price)
                else:
                    print("Expected Result: Price = 22")
                    print(price)
            elif add_pepperoni == "N" or add_pepperoni == "n":
                if extra_cheese == "Y" or extra_cheese == "y":
                    price = price + 1
                    print("Expected Result: Price = 21")
                    print(price)
                else:
                    print("Expected result: Price = 20")
                    print(price)            

        else:
            print("There seems to be a problem. Please check your entries!")
                
                


# Execute code here 👇    
orderSummary()
processOrder()