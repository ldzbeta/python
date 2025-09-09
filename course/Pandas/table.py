from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pickachu", "Squirtle"])
table.add_column("Type",["Electric","water"])
table.align="l"
print(table)