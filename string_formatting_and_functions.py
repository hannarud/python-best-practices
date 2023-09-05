
# Formatting
template = "{name}'s favorite number is {num}, {num} is {name}'s favorite number"
output = template.format(name="Kylie", num="8")
print(output)


pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

template = "The approximate population of {country} is {population:,.2f} mln."

for entry in pop_millions:
    country_name = entry[0]
    country_population = entry[1]
    output = template.format(country=country_name, population=country_population)
    print(output)
