import pdb


def main():
    import pyfiglet

    print("-- please adjust window width if banner looks messed up")
    my_banner = pyfiglet.figlet_format("                   welcome")
    print(my_banner)

    def my_introduction(name, my_class, date):
        print(f"{name}\n{my_class}\n{date}")

    my_introduction(
        "  Jason Preneveau", "  CMIS-120", "  19 June 2022 (updated 06 Oct 2022)\n"
    )


main()


_EXITLOOP = -99
question = int(input("Number of miles driven on Monday: "))
while question != _EXITLOOP:
    monday = question
    print(f"\n----------> You drove {question} miles on Monday.")

    monday = int(input("\nNumber of miles driven on Tuesday: "))
    print(f"\n----------> You drove {monday} miles on Tuesday.")

    while question != _EXITLOOP:
        tuesday = question
        tuesday = int(input("\nNumber of miles driven on Wednesday: "))
        print(f"\n----------> You drove {tuesday} miles on Wednesday.")

        while question != _EXITLOOP:
            wednesday = question
            wednesday = int(input("\nNumber of miles driven on Thursday: "))
            print(f"\n----------> You drove {wednesday} miles on Thursday.")
            while question != _EXITLOOP:
                thursday = question
                thursday = int(input("\nNumber of miles driven on Friday: "))
                print(f"\n----------> You drove {thursday} miles on Friday.\n")
                while (
                    True
                ):  # I could not ggte program to stop looping so I came up with this
                    break
                break
            break
        break
    break


def average(my_list):
    average = sum(my_list) / len(my_list)
    return average


my_list = [question, monday, tuesday, wednesday, thursday]

avg_gas = average(my_list)
print(f"{avg_gas} Is your average number of miles this week.")
