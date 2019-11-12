def even_or_odd(n):
    if(n % 2 == 0):
        print("even")
    else:
        print("odd")

num  = input("Enter your number: ")
converted_num = int(num)
even_or_odd(converted_num)
