numero1 = int(input("Enter the 1st number: "))
numero2 = int(input("Enter the 2nd number: "))

print("Choose operator: ")
print("1 [+]")
print("2 [-]")
print("3 [x]")
print("4 [÷]")

choice = int(input("Enter operator: "))

if choice == 1:
    result = numero1 + numero2

elif choice == 2:
    result = numero1 - numero2

elif choice == 3:
    result = numero1 * numero2

elif choice == 4:
    if numero2 == 0:
        print("Error: You cannot divide by zero.")
        exit()
    else:
        result = numero1 / numero2
else:
    print("Wrong! Try again.") 
    exit()

print("Calculation Results: ")

if choice == 4:
    print("Answer:", float(result))
else:
    print("Answer:", int(result))