#python slicing
def tuple_slice(startIndex, endIndex, tup):
    return None

if __name__ == "__main__":
    print(tuple_slice(1, 4, (76, 34, 13, 64, 12)))

def tuple_slice(start_index, end_index, tup):
    return tup[start_index:end_index]

print(tuple_slice(1, 4, (76, 34, 13, 64, 12)))  # Output: (34, 13, 64)



class Greeter:

    def __init__(self, boss):
        pass

    def enters(self, visitor):
        return None

    def greet(self):
        pass
    
if __name__ == "__main__":
    g = Greeter('Chuck')
    g.enters('John')
    print(g.greet())