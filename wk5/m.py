import math

G = 6.674*(10**(-11))

def force(m1, m2, d):
  F = (G*m1*m2)/(d**2)
  return F


def distance(m1, m2, F):
  d = math.sqrt( (G*m1*m2)/F )
  return d


def mass(m1, F, d):
    m2 = (F*(d**2)) / (G*m1)
    return m2


def get_input(input_request):
    try:
        out = float(input(input_request))
    except:
        print('please only enter numeric values.')
    return out


n = input("Solve for force, distance, or mass. Input one: ")

if n == 'force':
    m1 = get_input("Enter m1: ")
    m2 = get_input("Enter m2: ")
    d = get_input("Enter d: ")
    print(force(m1, m2, d) )
elif n == 'distance':
    m1 = get_input("Enter m1: ")
    m2 = get_input("Enter m2: ")
    F = get_input("Enter F: ")
    print(distance(m1, m2, F))
elif n == 'mass':
    m1 = get_input("Enter m1: ")
    F = get_input("Enter F: ")
    d = get_input("Enter d: ")
    print(mass(m1, F, d))
else:
    print("Please enter: 'force', 'distance', or 'mass'")
