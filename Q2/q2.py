def main():
    import csv
    f = open('q2.csv', 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')
    header = next(data)
    lines = 0
    max_temp = 0
    max_date = ''
    min_temp = 999
    min_date = ''

    for row in data:
        if (len(row[2]) != 0) and (len(row[3]) != 0) and (len(row[4]) != 0):
            lines = lines + 1
            row[2] = float(row[2])
            row[3] = float(row[3])
            row[4] = float(row[4])
            day_temp = row[4]-row[3]  
            if max_temp < day_temp:
                max_date = row[0]
                max_temp = day_temp
            if min_temp > day_temp:
                min_date = row[0]
                min_temp = day_temp
        

    print('*'*3,'Annual Temperature Report for Seoul in 2022','*'*3,"\n")
    print("Day with the Largest Temperature Variation:",max_date,"\n")
    print("Maximum Temperature Difference:",round(max_temp,1),"Celsius","\n")
    print("Day with the Smallest Temperature Variation:",min_date,"\n")
    print("Minimum Temperature Difference:",round(min_temp,1),"Celsius","\n")
    
    f.close()    

if __name__ == '__main__':
    main()
