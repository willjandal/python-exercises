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
def order_summary():
    print("[+] Order Summary")
    if size == "S" or size == "s":
        print(f"[+] Pizza Size: Small")
    print(f"[+] Additional Pepperoni: {add_pepperoni}")
    print(f"[+] Additional Cheese: {extra_cheese}")
    return


# Execute code here 👇
    
order_summary()

# need to make this a function
if size == "S" or size == "s":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        if extra_cheese == "Y" or extra_cheese == "y":
            print(f"You've ordered a Small sized pizza with Pepperoni and Extra Cheese!")
            print("Total bill: $18!")
        else:
            print(f"You've ordered a Small sized pizza with Pepperoni!")
            print("Total bill: $17!")
    else:
        print(f"You've ordered a Small sized pizza!")
        print("Total bill: $15!")
elif size == "M" or size == "m":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        if extra_cheese == "Y" or extra_cheese == "y":
            print(f"You've ordered a Medium sized pizza with Pepperoni and Extra Cheese!")
            print("Total bill: $23!")
        else:
            print(f"You've ordered a Medium sized pizza with Pepperoni!")
            print("Total bill: $22!")
    else:
        print(f"You've ordered a Medium sized pizza!")
        print(f"Total bill: $20!")
elif size == "L" or size == "l":
    if add_pepperoni == "Y" or add_pepperoni == "y":
        if extra_cheese == "Y" or extra_cheese == "y":
            print(f"You've ordered a {size} sized pizza with Pepperoni and Extra Cheese!")
            print("Total bill: $27!")
        else:
            print(f"You've ordered a {size} sized pizza with Pepperoni!")
            print("Total bill: $26!")
    else:
        print(f"You've ordered a {size} sized pizza!")
        print("Total bill: $25!")
else:
    print("There seems to be a problem, please check your entries!")   