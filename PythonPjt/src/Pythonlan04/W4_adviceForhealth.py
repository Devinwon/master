advice='偏瘦','正常','偏胖','肥胖'
#weight=float(input("Input weight："))
#height=float(input("Input height："))
#BMI=weight/(height**2)
BMI=float(input("Input BMI:"))
if BMI<18.5:
    print("International:"+advice[0])
    print("China:"+advice[0])
elif (BMI>=18.5 and BMI<24):
    print("International:"+advice[1])
    print("China:"+advice[1])
elif (BMI>=24 and BMI<25):
    print("International:"+advice[1])
    print("China:"+advice[2])
elif (BMI>=25 and BMI<28):   
    print("International:"+advice[2])
    print("China:"+advice[2])   
elif (BMI>=28 and BMI<30):   
    print("International:"+advice[2])
    print("China:"+advice[3])  
elif (BMI>=30):   
    print("International:"+advice[3])
    print("China:"+advice[3])   