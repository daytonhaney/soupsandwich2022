# The special name varibale in Python
# - Entry Point
#

# import assignment_pw_builder

print(f"imported bad script ")


def useful_function(x):
    return x * x - 2


class UsefulClass:
    def __init__(self, x):
        self.x = x


if __name__ == '__main__':
    for i in range(8):
        print(useful_function(i))
