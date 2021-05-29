"""
    AUTHOR: GAUTAM CHANDRA SAHA
    DATE & TIME: 29/05/21 AT 4:26 PM

"""

number = 7

user_input = int(input("Enter a number: "))

if user_input == number:
    print("You guessed it correct!")
elif user_input - number in (1, -1):
    print("Yor were off by one!")
else:
    print("You guessed it wrong!")
