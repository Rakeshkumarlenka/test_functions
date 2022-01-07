from prettytable import PrettyTable

myTable = PrettyTable(["Name","Id","Salary"])
myTable.add_row(["Rakesh","001","70k"])
myTable.add_row(["Sohel","005","80k"])
myTable.add_row(["Ramesh","041","20k"])
myTable.add_row(["harish","301","20k"])
myTable.add_row(["keshu","031","80k"])
myTable.add_row(["Akash","011","40k"])
myTable.add_row(["rabi","021","40k"])
print(myTable)
