import csv
with open('height-weight.csv',newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []

for i in range (len  (file_data)):
    n_num = file_data[i][1] 
    new_data.append(float(n_num))
    

#getting the mean/ calculating the mean

n = len(new_data)
new_data.sort()

#using the floor division
if n%2 == 0  :

    #getting the first number
    median1 = float(new_data[n//2])
    #getting the second number
    median2 = float(new_data[n//2 + 1])
 
    median = (median1 + median2)/2

else:

    median = new_data[n//2]
    print(n)

print("median is:-" + str(median))

    


