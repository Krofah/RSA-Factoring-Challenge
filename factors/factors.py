import sys

def factorize(num):
    """
    Factorizes a number into a product of two smaller numbers
    """
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return f"{num}={i}*{num//i}"
    return f"{num}={num}*1"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        for line in f:
            num = int(line.strip())
            print(factorize(num))

