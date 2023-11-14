def main():
    print("miniräknare")


matte = input("\n\tMata in vilket räknesätt du vill använda. 1. Plus 2. Minus 3. Multiplikation 4. Division\n")
if (matte == "1"):
    print("Du har valt plus.")
    nummer1 = int(input("\n\tMata in ditt första nummer\n"))
    nummer2 = int(input("\n\tMata in ditt andra nummer\n"))
    print(nummer1 + nummer2)

if (matte == "2"):
    print("Du har valt Minus.")
    nummer1 = int(input("\n\tMata in ditt första nummer\n"))
    nummer2 = int(input("\n\tMata in ditt andra nummer\n"))
    print(nummer1 - nummer2)

if (matte == "3"):
    print("Du har valt Multiplikation.")
    nummer1 = int(input("\n\tMata in ditt första nummer\n"))
    nummer2 = int(input("\n\tMata in ditt andra nummer\n"))
    print(nummer1 * nummer2)

if (matte == "4"):
    print("Du har valt Division.")
    nummer1 = int(input("\n\tMata in ditt första nummer\n"))
    nummer2 = int(input("\n\tMata in ditt andra nummer\n"))
    print(nummer1 / nummer2)

