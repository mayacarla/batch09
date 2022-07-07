#CSCI 127
#Maya Anderson
#this function rq. a non-empty string

mess = input("Enter a non-empty string: ")


while len(mess) == 0:
    print("That was empty. Try again.")
    mess = input("Enter a non-empty string: ")

print("You entered: ", mess)
