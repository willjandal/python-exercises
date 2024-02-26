print("Thank you for choosing Python Pizza Deliveries!")

#price list
#Small Pizza (S) = 15
#Medium Pizza (M) = 20
#Large Pizza (L) = 25
#Additional pepperoni = 2
#Additional cheese = 1

size = input("What size of pizza do you want? S, M, or L: ") #What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want to add pepperoni? [Y or N]: ") # Do you want to pepperoni? Y or N
extra_cheese = input("Do you want to add extra cheese? [Y or N]: ") #Do you want extra cheese? Y or N


# 🚨 Don't change the code above 👆

# Write your code below this line 👇
print(f"Pizza Size: {size}")
print(f"Additional Pepperoni: {add_pepperoni}")
print(f"Additional Cheese: {extra_cheese}")


if size == "S" or "s":
    print(15)
else:
    print("Hello World")