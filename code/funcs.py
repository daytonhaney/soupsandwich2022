

delux_indoor_price = 150
reg_indoor_price = 75
outdoor_package = 100


def size_of_house(length, width):
    """When the workers are on-site, they take the 

        measurments of the house"""
    
    return length * width


indoor_regular = [
    "Dust",
    "Sweep",
    "Vacuum",
    "General Tidying",
    "Senior Discount",
    float(100.00)

]


indoor_delux = [
    "Regular Services + ",
    "Bathrooms",
    "Bedrooms",
    "Discount",
    "Senior Discount",
    float(200.00)


]
outdoor_services = [
    "Mowing",
    "Pruning",
    "WeedWacking",
    "Pressure Wash",
    float(200.00)
]


"""
trim = "trim shrubs"
prune = 15
mow = "trim the bushes"
print('{:<13}{:^20}{:<20} {:>10}'.format("Indoor Services",
      "Outdoor Services", "FT WEEKLY SALARY", "PT WEEKLY SALARY"))

print('{:<10}{:^22}{:>15}{:>20}'.format("1.00$", ".25$", "20.00", "10.00"))
#print(ui, '\n')
x = '{:<10}{:^22}{:>15}{:>20}'.format("1.00$", ".25$", "20.00", "10.00")
print(x)
print(x[:])
b = "{}"
ask = []
d = [[3], 1, 2.2]
e = ""
print(d)
  
  """
