multiplier = 0

while multiplier <= 10:
    print(f"Table de {multiplier}:", end=" ")
    i = 0
    while i <= 10:
        print(multiplier * i, end=" " if i < 10 else "\n")
        i += 1
    multiplier += 1
