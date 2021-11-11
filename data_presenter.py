# Problem 2
cupcake = open("CupcakeInvoices.csv")

# Problem 3
for rows in cupcake:
    print(rows)

#Problem 4
for rows in cupcake:
    values = rows.split(',')
    print(values[2])

#Problem 5
for rows in cupcake:
  values = rows.split(',')
  total = int(values[3]) * float(values[4])
  print(total)

  # Problem 6
total = 0

for rows in cupcake:
  values = rows.split(',')
  total = total + (int(values[3]) * float(values[4]))
print(total)

# Problem 7
cupcake.close()

