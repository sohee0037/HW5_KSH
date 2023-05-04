def main():
    import csv

    def find_max(line):
        f = open('q4.csv', 'r', encoding='UTF-8')
        data = csv.reader(f, delimiter=',')
        header = next(data)
        mx=0
        station_mx = ""
        for row in data:
            if row[1] == line:
                row[4] = float(row[4])
                if mx < row[4]:
                    mx = row[4]
                    station_mx = row[3]
        f.close()
        print("Busiest Station: %s (%1d)"%(station_mx,mx))

    def find_min(line):
        f = open('q4.csv', 'r', encoding='UTF-8')
        data = csv.reader(f, delimiter=',')
        header = next(data)
        mn=99999999
        station_mn = ""
        for row in data:
            if row[1] == line:
                row[4] = float(row[4])
                if mn > row[4]:
                    mn = row[4]
                    station_mn = row[3]
        f.close()
        print("Least Station: %s (%1d)"%(station_mn,mn))

    print('*'*3,"Subway Report for Seoul on March 2023",'*'*3,"\n")
    for i in range(1,5):
        print("Line",i)
        find_max("%d호선"%i)
        find_min("%d호선"%i)
        print("")

if __name__ == '__main__':
    main()
