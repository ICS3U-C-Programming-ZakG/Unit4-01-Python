#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Nov. 2, 2023
# This program gets a number from the user and will use a while loop to calculate the total sum from 0 to the inputted number.


def main():
    # declare variables
    counter = 0
    sum = 0

    # introduce program to user
    print(
        "This program gets a positive integer from the user and will calculate the total sum from 0 to the inputted number"
    )

    # get user input
    user_num_str = input("Please enter a positive integer: ")

    # try casting user input into an integer
    try:
        user_num_int = int(user_num_str)

        # check if user number is a positive integer
        if user_num_int >= 0:
            # loop while counter is less than user number execute following code
            while counter <= user_num_int:
                # while (counter <= user_num_int):

                # adding 1 to the new sum every time it loops
                sum = sum + counter

                # add 1 to the counter every time
                counter = counter + 1

                # displaying the amount of times the program loops
                print("Tracing {} times through the loop.".format(counter))

            # displaying the result sum of the inputted number
            print("The sum of numbers from 0-{} is {}.".format(user_num_int, sum))

        # if number is negative tell user
        else:
            print(
                "{} is an invalid input, it must be a positive integer.".format(
                    user_num_int
                )
            )

    # catch invalid inputs from user
    except Exception:
        print("{} is not a positive integer.".format(user_num_str))


if __name__ == "__main__":
    main()
