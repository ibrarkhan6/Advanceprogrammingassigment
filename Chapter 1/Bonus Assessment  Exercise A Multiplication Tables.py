# Using below the def function.
def print_multiplication_table():
    for a in range(1, 11):
        print(f"\nMultiplication Table for {a}:")
        for b in range(1, 11):
            result = a * b
            print(f"{a} x {b} = {result}")
# Using the if function below.
if __name__ == "__main__":
    print_multiplication_table()
