
def multiplication_table(num, upto=10):
    print(f"Multiplication Table for {num}:")
    for i in range(1, upto + 1):
        print(f"{num} x {i} = {num * i}")


number = int(input("Enter the number for which you want the multiplication table: "))
upto = int(input("Enter how many multiples you want (default is 10): ")) or 10

multiplication_table(number, upto)
