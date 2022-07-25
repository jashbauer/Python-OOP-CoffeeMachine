
from prettytable import PrettyTable

table = PrettyTable()
print(table)

pokemon_data = {
    "Pokemon Name": ["Pikachu", "Bubasaur", "Squirtle", "Charmander"],
    "Pokemon Type": ["Electric", "Plant", "Water", "Fire"]
}

# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Bubasaur"])
for key in pokemon_data:
    table.add_column(key, pokemon_data[key])

print(table.align)
table.align = "l"
print(table)