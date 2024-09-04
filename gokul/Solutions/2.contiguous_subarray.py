def max_sum(arr):
    if not arr:
        raise ValueError("Empty array")
    max_value = arr[0]
    max_last  = arr[0]
    for i in range(1, len(arr)):
        max_last  = max(arr[i], max_last  + arr[i])
        max_value = max(max_value, max_last )
    return max_value

def main():
    # Get input from the user
    user_input = input("number=")
    # string to int
    try:
        number = list(map(int, user_input.split(',')))
    except ValueError:
        print("Invalid input")
        return
    # calculate and print output
    try:
        result = max_sum(number)
        print("Output=", result)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
