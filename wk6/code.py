
"""
my_secrets = ["lion", "pig", "    ", "cow", "cat", "dog"]

secret_answer = input(
    "\nEnter Secret Word:  \n\n'hint: 3 letter animal'\t\t\t")

try:
    my_secrets.index(secret_answer)
except ValueError:
    print("\n\t\t\tMatch not found!\n")

else:
    print("\n\t\t\tMatch Found! Welcome\n")
"""


def get_average(quartly_totals):
    my_sums = sum(quartly_totals)
    my_totals = len(quartly_totals)
    average_quartly_total = my_sums / my_totals
    return average_quartly_total


quartly_totals = [10, 20, 20, 34, 22, 32, 23, 35]
average_quartly_total = get_average(quartly_totals)
print(f"{quartly_totals}")
print(f"{average_quartly_total}")
