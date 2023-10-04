a = 101
b = 22

def foo():
    b = 1
    print(b)
    # E englobant puis il remonte
    def baz():
        # Python b regarde localement L
        c = 11
        print(c)
        print(b)
        print(a)

    baz()

    return "scope"

print( foo() )

