#open file for reading
import csv

infile = open('steps.csv','r')

csv_obj = csv.reader(infile, delimiter = ',')
header = next(csv_obj)

jan = 31
feb = 28
march = 31
april = 30
may = 31
june = 30
july = 31
august = 31
sept = 30
october = 31
nov = 30 
dec = 31 
#januray calc 
step = 0 
for i in range(jan):
    row = next(csv_obj)
    step += int(row[1])
avg = step/jan

print(f"Janurary - {avg:,.2f}")

#febuary calc 
step = 0
for i in range(feb):
    row = next(csv_obj)
    step += int(row[1])
avg = step/feb
print(f"Febuary - {avg:,.2f}")

#march calc 
step = 0 
for i in range(march):
    row = next(csv_obj)
    step += int(row[1])
avg = step/march
print(f"March - {avg:,.2f}")

#april calc 
step = 0 
for i in range (april):
    row = next(csv_obj)
    step += int(row[1])
avg = step/april
print(f"April - {avg:,.2f}")

#may calc
step = 0 
for i in range(may):
    row = next(csv_obj)
    step += int(row[1])
avg = step/may
print(f"May - {avg:,.2f}")

#June calc
step = 0 
for i in range(june):
    row = next(csv_obj)
    step += int(row[1])
avg = step/june
print(f"June - {avg:,.2f}")

#july calc
step = 0 
for i in range(july):
    row = next(csv_obj)
    step += int(row[1])
avg = step/july
print(f"July - {avg:,.2f}")

#august calc 
step = 0 
for i in range(august):
    row = next(csv_obj)
    step += int(row[1])
avg = step/august
print(f"August - {avg:,.2f}")

#September calc
step = 0 
for i in range(sept):
    row = next(csv_obj)
    step += int(row[1])
avg = step/sept
print(f"Septeber - {avg:,.2f}")

#october calc
step = 0 
for i in range(october):
    row = next(csv_obj)
    step += int(row[1])
avg = step/october
print(f"October - {avg:,.2f}")

#November calc
step = 0 
for i in range(nov):
    row = next(csv_obj)
    step += int(row[1])
avg = step/nov
print(f"November - {avg:,.2f}")

#December calc
step = 0 
for i in range(dec):
    row = next(csv_obj)
    step += int(row[1])
avg = step/dec
print(f"December - {avg:,.2f}")

infile.close

