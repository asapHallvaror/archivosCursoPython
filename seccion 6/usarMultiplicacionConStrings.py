print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

x = int(input())
y = int(input())
 
x = x // y
y = y // x
 
print(y)