# get two integer parameters
# return sum
def plus(x, y):
    return x+y

# check if it is integer
def check_integer(s):
    while True:
        if s.isdigit():
            return int(s)
        else:
            print("Put integer")
            s = input()

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >=1:       
        print("0: exit, 1: plus")
        check = check_integer(input())
        if check == 1:
            print("First Number")
            x = check_integer(input())
            print("Second Number")
            y = check_integer(input())
            print("answer : ", plus(x,y))
        elif check > 1:
            print("Unsupported")
        else:
            print("Thank you")

            

if __name__ == "__main__":
    main()