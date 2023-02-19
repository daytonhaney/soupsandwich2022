def userfunctions():

    regular = [
        "General Tidying",
        "Sweep",
        "Dust",
        "Mop",

    ]
    premium = [
        "Regular Services + ",
        "Bathrooms",
        "Closets",
        "Discount",
        "Senior Discount",


    ]
    outdoor = [
        "Mowing ",
        "Pruning",
        "WeedWhacking",
        "Pressure Wash",
    ]

    total_services = {
        "regular": ["General tidying", "Sweep", "Dust", "Mop"],
        "premuim": ["Regular Service", "Bathroom", "Closets", "Discount", "Senior Discount"],
        "outdoor": ["Mowing", "Pruning", "Weed-Whacking", "Senior-Discount"]

    }

    print(total_services.keys)
    for _ in total_services:
        print(_)


userfunctions()
