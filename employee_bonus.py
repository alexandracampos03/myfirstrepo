import csv

infile = open('employee_data.csv', 'r')

csv_obj = csv.reader(infile, delimiter = ',')

header = next(csv_obj)

for rec in csv_obj:
    bonusrate = float(rec[7])
    salary = float(rec[3])
    bonuspay = (bonusrate * salary)
    pay = (salary + bonuspay)
    print(f"Name: {rec[1]}")
    print(f"Salary: $ {salary:>10,.2f} ")
    print(f"Bonus:  $ {bonuspay:>10,.2f}")
    print(f"Pay:    $ {pay:>10,.2f}")

    input()