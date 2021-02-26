# Discuission 6 Debugger Demo

# return square of num
def return_square(num):
    square = 0
    square = num * num * num
    return square

# main function
def main():
    a = 3
    b = 4
    c = b

    # I want to get 9 (3x3) because c is 3
    d = return_square(c)
    print(d)
    print("Done")

main()
