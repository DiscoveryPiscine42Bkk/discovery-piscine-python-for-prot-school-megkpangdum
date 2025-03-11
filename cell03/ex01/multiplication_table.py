def multiplication_table(number):
    print(f"multiplication {number}")
    i = 1 
    while i <=12:
        print(f"{number} x {i} = {number * i}")
        i += 1
number = int(input("Enter the number: "))
multiplication_table(number)