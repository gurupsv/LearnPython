# Decorators
# All Decorators are clousures
# demo is decorators function
# sayhi is decorated function


def demo(a):
    def inner(b):
        def innermost():
            print("This is innermost -> ", a, b)
        return innermost
    return inner

@demo("Testing it")
def sayhi():
    print("Hi from sayhi!")


sayhi()
