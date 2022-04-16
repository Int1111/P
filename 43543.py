def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


#@makebold
@makeitalic
def hello():
    return "hello habr"
print(hello())
def who(func):
    def w():
        return func()
    return w
@who
def x():
    return 'g'
print(x())