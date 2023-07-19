###############
# ERIC FONTES #
###############

def encode(pwd):
    return "".join( str((int(num) + 3) % 10) for num in pwd )

# Fernando's code
def decode(pwd):
    out = ""

    for dig in pwd:

        invert = ((int(dig)+10)-3)%10
        out += str(invert)

    return out


def main():
    password = ""

    while True:
        print("Menu",
              "-------------",
              "1. Encode",
              "2. Decode",
              "3. Quit",
              "", sep="\n")
        option = input("Please enter an option: ")

        # Encode
        if option == "1":
            password = encode(input("Please enter your password to encode: ")) # password is UPDATED to encoded password
            print("Your password has been encoded and stored!")
            print()

            pass

        # Decode
        elif option == "2":
            print(f"The encoded password is {password}, ", end="")
            password = decode(password) # password is UPDATED to decoded password
            print(f"and the original password is {password}.")
            print()

            pass
        
        # Quit
        elif option == "3":
            break

        # print password for testing purposes
        elif option == "4":
            print(password)

main()
