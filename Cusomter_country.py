 

import csv

infile = open('customers.csv','r')
csv_obj = csv.reader(infile, delimiter = ',')
header = next(csv_obj)

outfile = open('cusomter_country.csv','w')
outfile.write("Full Name,Country \n")
count = 0 
for rec in csv_obj: 
    outfile.write(f"{rec[1]} {rec[2]},{rec[4]}\n")
    count += 1

outfile.write(f"The total number of customers is: {count}")


infile.close
outfile.close    






