def even_or_odd(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")


def square(x):
    row = "#"*x
    for i in range(x):
        print(row)
n = input("enter squares: ")
square(int(n))
