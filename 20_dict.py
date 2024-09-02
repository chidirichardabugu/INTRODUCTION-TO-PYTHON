# create a python dictionary with keys as the names of three countris & value as their capital.print the capitalof the second country
countrise_and_capital = {
    "Nigria": "Abuja",
    "England": "London",
    "Ghana": "Acara"
}
#method 1
print(countrise_and_capital["England"])

#method 2
second_country = list(countrise_and_capital.keys())[1]
capital_of_second_country = countrise_and_capital[second_country]
print(capital_of_second_country)