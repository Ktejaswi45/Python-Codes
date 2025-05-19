def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

start = int(input("Enter start limit: "))
end = int(input("Enter end limit: "))

print(f"Factorials from {start} to {end}:")
for i in range(start, end + 1):
    print(f"{i}! = {factorial(i)}")
