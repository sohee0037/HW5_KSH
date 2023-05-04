def main():
    import csv
    f = open('q1.csv', 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')
    header = next(data)
    lines = 0
    avr_1 = 0
    avr_2 = 0
    avr_3 = 0
    for row in data:
        if (len(row[2]) != 0) and (len(row[3]) != 0) and (len(row[4]) != 0):
            lines = lines + 1
            row[2] = float(row[2])
            row[3] = float(row[3])
            row[4] = float(row[4])
            avr_1 += row[2]
            avr_2 += row[3]
            avr_3 += row[4]

    avr_1=avr_1/lines
    avr_2=avr_2/lines
    avr_3=avr_3/lines

    print('*'*3,'Annual Temperature Report for Seoul in 2022','*'*3,"\n")
    print("Average Temprature:",round(avr_1, 2),"Celsius","\n")
    print("Average Minimum Temprature:",round(avr_2, 2),"Celsius","\n")
    print("Average Maximum Temprature:",round(avr_3, 2),"Celsius","\n")
    
    f.close()    

if __name__ == '__main__':
    main()
