#
# zum temporären testen...
#

#variables
in_number = 0
counter = 0

print("WELCOME TO FIZZBUZZ WHERE WE HAVE MODERATE FUN WITH NUMBERS!")
print(" ")

while True:
    in_number = int(input("Please enter a number between 1 and 100: "))
    if 0 < in_number < 101:
        for counter in range(1, in_number+1):
            if counter % 3 == 0 and counter % 5 == 0:
                print("fizzbuzz")
            elif counter % 3 == 0:
                print("fizz")
            elif counter % 5 == 0:
                print("buzz")
            else:
                print(counter)
        counter = counter + 1
        break

    else:
        print("Please try to follow the instructions.")