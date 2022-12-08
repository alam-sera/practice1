weight = int(input("Enter your weight! "))
choice = input("(L)bs or (K)g")
if choice.upper() == "L":
    print(weight * 0.45)
elif choice == "K":
    print(weight * 2.2)
