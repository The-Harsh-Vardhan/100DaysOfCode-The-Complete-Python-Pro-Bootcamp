#PRETTY TABLE
from prettytable import PrettyTable
table = PrettyTable()
print(table)

#Read the documentation for help

#Adding column and Data
table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

print(table)

table.align = "l"

print(table)