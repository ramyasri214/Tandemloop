

a = int(input("Enter a number: "))

odd_numbers = [2*i + 1 for i in range(a)]

print(", ".join(map(str, odd_numbers)))
