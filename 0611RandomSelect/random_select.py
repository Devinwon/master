
import csv


csvfile = open('lucky2.csv', 'r')
reader = csv.reader(csvfile)
data = []

for line in reader:
    data.append(line)

data = data[1:]

# data = [['1','机器猫1'],['2','机器猫2'],['3','机器猫3'],['4','机器猫4'],['5','机器猫5'],['6','机器猫6'],['7','机器猫7'],['8','机器猫8']]

import random
import time

luckys = []

for i in range(1,51):
    lucky = random.choice(data)
    print('  ', lucky[0],lucky[1])
    data.remove(lucky)
    luckys.append(lucky[0]+'号-'+lucky[1])
    time.sleep(1)


print('\nLucky Boys：', luckys,'\n')
# csvfile.close()