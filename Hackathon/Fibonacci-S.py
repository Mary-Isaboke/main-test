
    
def fibonacci_sequence(n):
    sequence = [0, 1]  # Initialize Fibonacci sequence with first two terms
    
    if n <= 2:
        return sequence[:n]  # Return sequence with first n terms if n is 1 or 2
    
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]  # Calculate next Fibonacci term
        sequence.append(next_term)  # Add next term to sequence
    
    return sequence

def main():
    n = int(input("Enter the value of n: "))  # Ask user to input the value of n
    fibonacci = fibonacci_sequence(n)  # Generate Fibonacci sequence
    
    print("Fibonacci sequence up to term", n, "is:", fibonacci)  # Print generated Fibonacci sequence

if __name__ == "__main__":
    main()
