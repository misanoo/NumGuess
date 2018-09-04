import random

def replay_again():
    again = input("You have run out of guesses! Would you like to play again? Y/N")
    if again == 'y' or again == 'Y':
        guesser()
    elif again == 'n' or again== 'N':
        print("Thanks for playing! Have a nice day!")
        exit()
    else:
        print("That is not a vlid answer.")
        answer_again = input("Next time, input Y or N! Play again? Y/N")
        if answer_again == 'y' or answer_again == 'y':
            guesser()
        elif answer_again == 'n' or answer_again == 'N':
            print("Thanks for playing! Have a nice day!")
            exit()

def guesser():
    print("Welcome to Wesley's number generator game!")
    print("In this game a number is randomly generated between two numbers you select.")
    print("You then have a number of tries to guess the generated number. The number of tries you are given is equal to the max number - the min number. Example: min = 50, max = 100, tries = 100 - 50 = 50. Goodluck and have fun!")

    try:
        minnum = int(input("Please type the min number in the range for number generator: "))
        maxnum = int(input("Please type the max number in the range for number generator: "))
    except ValueError:
        print("That is not a number.")
        answer = input("Next time, input a number please! Play again? Y/N")

        if answer == 'y' or answer == 'Y':
            guesser()
        elif answer == 'n' or answer == 'N':
            print("Thanks for playing! Have a nice day!")
        else:
            print("Not a valid answer! Goodbye!")

    gen = random.randint(minnum, maxnum)
    tries = 0
    triesleft = (maxnum / 2)
    print("A number between", minnum, "and", maxnum, "has been generated, try and guess it in", triesleft, "guesses.")

    while triesleft != 0:

        try:
            guess = int(input("Enter your guesss: "))
        except ValueError:
            print("That is not a number.")
            answer = input("Next time, input a number please! Play again? Y/N")

            if answer == 'y' or answer == 'y':
                guesser()
            elif answer == 'n' or answer == 'N':
                print("Thanks for playing! Have a nice day!")
                break
            else:
                print("Not a valid answer! Goodbye!")
                break

        else:
            if guess != gen:
                if triesleft == 0:
                    answer = input("You ran out of tries, try again? Y/N")
                    if answer == 'y' or answer == 'y':
                        guesser()
                    if answer == 'n' or answer == 'N':
                        print("Thanks for playing! Have a nice day!")
                        break
                    if answer != 'y' and answer != 'Y' and answer != 'n' and answer != 'N':
                        print("Not a valid response!Goodbye!")
                        break

                elif guess < minnum or guess > maxnum:
                    print("Guess not between", minnum, "and", maxnum, "try again!")
                    triesleft == triesleft

                elif guess < gen:
                    triesleft = triesleft - 1
                    print("Your guess is too low. You have {} tries left".format(triesleft))
                    if triesleft == 0:
                        replay_again()

                elif guess > gen:
                    triesleft = triesleft - 1
                    print("Your guess is too high. You have {} tries left.".format(triesleft))
                    if triesleft == 0:
                        replay_again()
            else:
                answer = input("YAY! You won! Do you want to play again? Y/N")
                if answer == 'y' or answer == 'y':
                    guesser()
                if answer == 'n' or answer == 'N':
                    print("Thanks for playing! Have a nice day!")
                    break

guesser()




