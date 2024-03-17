print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆

# Functions 👇

#proccess the count

def countFirstName(lower_names):
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")

    first_digits = t + r + u + e
    second_digits = l + o + v + e

    final_score = int(str(first_digits) + str(second_digits))
    print(final_score)

    #evaluate the score
    if final_score < 10:
        print(f"Your score is {final_score}, you go together like coke and mentos.")
    elif final_score > 90:
        print(f"Your score is {final_score}, you go together like coke and mentos.")
    elif final_score < 50 and final_score > 40:
        print(f"Your score is {final_score}, you are alright together.")
    else:
        print(f"Your score is {final_score}.")
    return final_score
    

# Write your code below this line 👇

combine_names = name1 + name2
lower_names = combine_names.lower()

countFirstName(lower_names)

#hello
