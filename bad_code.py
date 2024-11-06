def f(x):
    if x > 0:
        return True
    else:
        return False


def do_stuff(a, b):
    c = 0
    for i in range(1000000):
        c += i
    print("The result is: " + str(c))
    if f(a):
        print("A is positive")
    else:
        print("A is not positive")

    if f(b):
        print("B is positive")
    else:
        print("B is not positive")


def main():
    do_stuff(5, -10)
    do_stuff(0, 3)
    do_stuff(-1, -2)


if __name__ == "__main__":
    main()