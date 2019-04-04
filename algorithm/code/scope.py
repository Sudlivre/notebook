"""
作用域 - Local -> Embedded -> Global -> Built-in
"""
def foo():
    x = 300

    def bar():
        nonlocal x
        x = 200
        print(x)

    bar()
    print(x)


if __name__ == '__main__':
    foo()
