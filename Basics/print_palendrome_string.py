def generate_numeric_palindrome_string(n):
    # Generates a palindrome like 123...n...321
    res = []
    for i in range(1, n + 1):
        res.append(str(i))
    for i in range(n - 1, 0, -1):
        res.append(str(i))
    return "".join(res)

if __name__ == "__main__":
    n = 9
    print(f"Palindrome for n={n}:")
    print(generate_numeric_palindrome_string(n))

    print("\nIdentity check:")
    balance = 1000
    new_balance = 1000
    print(f"balance id: {id(balance)}")
    print(f"new_balance id: {id(new_balance)}")
    print(f"Are they same object? {balance is new_balance}")

    balance += 250
    print(f"After modification, balance: {balance}")
    print(f"balance id: {id(balance)}")
    print(f"new_balance id: {id(new_balance)}")
