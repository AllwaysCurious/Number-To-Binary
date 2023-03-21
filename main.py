def array_to_string(array):
    result_string = ""
    for i in array:
        result_string += str(i)
    return result_string

while True:
    input_val = input("Enter a number to convert to binary (Type '/' to switch servers or 'exit' to close the program): ")
    if input_val == "/":
        switch = not switch
    elif input_val == "exit":
        break
    else:
        try:
            success_input = abs(int(input_val))
        except ValueError:
            print("Please only enter numbers!")
            continue
        bits = []
        start_val = 1
        while start_val <= success_input:
            bits.append(start_val)
            start_val *= 2
        result_bin = []
        for bit in reversed(bits):
            if success_input >= bit:
                result_bin.append(1)
                success_input -= bit
            else:
                result_bin.append(0)
        print(f"{input_val} is {array_to_string(result_bin)} in Binary")