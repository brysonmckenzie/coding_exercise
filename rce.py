import csv


print('Enter First Name:')
x = input()
print(x)

print('Enter Middle Name:')
y = input()
print(y)
print('Enter Last Name:')
z = input()
print(z)



f = open("data.csv", "r+")
csv_f = csv.reader(f)
for row in csv_f:
    print(row)
f.close()

with open("data.csv", "r+") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
    f.close()

with open("data.csv", "r+") as f:
    writer = csv.writer(f)
    writer.writerow(["First", "Middle", "Last"])
    output = writer.writerow([x, y, z])
    f.close()

