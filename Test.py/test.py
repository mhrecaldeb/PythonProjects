#test.py

#print(print)
# a = (isinstance(print, object))
# print(a)

def add(a, b):
    def prev(x):
        return x - 1
    return prev(a) + prev(b) + 2


# a = add(int(input("Ingresa un entero: \n")), int(input("Ingresa otro entero: \n")))
# print(f"El resultado es {a}")

def first(l):
    return l[0]

def last(l):
    return l[-1]

def list_index_factory(index_wanted):
    def indexer(l):
        return l[index_wanted]
    return indexer

# first = list_index_factory(0)
# last = list_index_factory(-1)
# l = [4, 29, 584, 73]
# print(first(l))

# print(last(l))


def debugger_teacher(func):
    def new_func_that_debugs(a, b):
        print(f"In '{func.__name__}' w/ args {a = }, {b = }.")
        ret = func(a, b)
        print(f"Returning with {ret = }.")
        return ret
    return new_func_that_debugs



@debugger_teacher
def add(a, b):
    def prev(x):
        return x - 1
    return prev(a) + prev(b) + 2

print(add(5, 8))
# debugger_add = debugger_teacher(add)
# print(debugger_add(4, 8))