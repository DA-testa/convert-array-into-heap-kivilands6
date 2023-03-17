# Edžus Kivilands   221RDB339
# python3


def build_heap(data):
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    swaps = []

    if n == 0:
        swaps.append(0)
        return swaps

    def swap(child, parent):
        swaps.append((parent, child))
        data[child], data[parent] = data[parent], data[child]

    def HeapUp(m):
        if m == 0:
            return
        if data[m] < data[(m-1)//2]:
            swap(m, (m-1)//2)
            HeapUp((m-1)//2)

    for i in range(n-1, -1, -1):
        HeapUp(i)
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    input_text = input()
    if 'F' in input_text:
        input_file = input()
        input_file = "tests/" + input_file
        if 'a' not in input_file:
            try:
                with open(input_file, "r") as f:
                    n = int(f.readline())          
                    data = list(map(int, f.readline().split()))

                    # checks if length of data is the same as the said length
                    assert len(data) == n

                    # calls function to assess the data 
                    # and give back all swaps
                    swaps = build_heap(data)

                    # TODO: output how many swaps were made, 
                    # this number should be less than 4n (less than 4*len(data))

                    # output all swaps
                    print(len(swaps))
                    for i, j in swaps:
                        print(i, j)

            except FileNotFoundError:
                return print("File_not_found_error")

    if 'I' in input_text:
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

        # checks if length of data is the same as the said length
        assert len(data) == n

        # calls function to assess the data 
        # and give back all swaps
        swaps = build_heap(data)

        # TODO: output how many swaps were made, 
        # this number should be less than 4n (less than 4*len(data))

        # output all swaps
        print(len(swaps))
        for i, j in swaps:
            print(i, j)

if _name_ == "_main_":
    main()