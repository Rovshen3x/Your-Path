name = input("Your Name: ")
print("Hello ", name, "Welcome to game!!")

x = input("Do you wanna play? ").lower()

if x == "yes":
    print("Welcome to road")
    y = int(input("Your 2 road at the end of city. Choose one of them ? (1/2)"))
    if y == 1:
        print("Your DEAD :)")
    elif y == 2:
        y = input("Your going to LA. Now your going to do choose the rest to eat (anna/beer) ?").lower()
        if y == "anna":
            print("Anna did not save you Your DEAD :)")
        else :
            print("beer not good DEAD")
    else :
        print('Your need valid caution Your DEAD :)')
else:
    print("Your DEAD")