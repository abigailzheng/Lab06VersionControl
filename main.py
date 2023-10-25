"""
Lab 6
Abigail Zheng
Class: COP3502C
Section: 12309
Description: password encoder/decoder
"""


def encode(password):
    # iterates through each digit in password and adds 3
    encoded_password = ""
    for char in password:
        encoded_password += str(int(char) + 3)
    return encoded_password


if __name__ == '__main__':
    user_input = None
    while user_input != 3:
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit
""")
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        if user_input == 2:
            print(f"The encoded password is {encoded_password}, and the original password is ")
