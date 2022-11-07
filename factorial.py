#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Nov 1, 2022
# A program that calculates a
# User input factorial.


def main():

    # Spacer
    print("")

    # Tries to get the user's number as an integer.
    try:
        inp_user_num = int(input("Enter a positive integer: "))

    # Exception if the input is not a integer
    except ValueError:
        input("Invalid input, enter a positive integer only!")

    # Checks if inputs less the 0
    if inp_user_num < 0:
        print("Invalid input, enter a positive integer only ")

    # Initializing counter and product variables
    else:
        loop_counter = 0
        product = 1

        # Code to be executed until inp_user_num is equal to the counter
        while True:
            loop_counter = loop_counter + 1
            product = product * loop_counter
            print("Tracked through loop {} times".format(loop_counter))
            if loop_counter >= inp_user_num:
                break
        # Displays user output

        print(("{}! = {}".format(inp_user_num, product)))


if __name__ == "__main__":
    main()
