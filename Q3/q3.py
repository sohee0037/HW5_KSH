def main():
    import csv

    def hap_line(line):
        f = open('q3.csv', 'r', encoding='UTF-8')
        data = csv.reader(f, delimiter=',')
        header = next(data)
        hap = 0
        for row in data:
            if row[1] == line:
                row[4] = float(row[4])
                row[5] = float(row[5])
                hap = hap+row[4]+row[5]
        f.close()
        return hap

    dic_hap = {}
    for i in range(1,10):
        dic_hap["%d호선"%i]=hap_line("%d호선"%i)
    sorted_values = sorted(dic_hap.values())

    sorted_dic = {}
    for value in sorted_values:
        for key in dic_hap:
            if dic_hap[key] == value:
                sorted_dic[key] = value
    sorted_keys = list(sorted_dic.keys())

    print('*'*3,"Subway Report for Seoul on March 2023",'*'*3,"\n")
    print("1st Busiest Line:",sorted_keys[-1],"(%1d)"%sorted_values[-1],"\n")
    print("2nd Busiest Line:",sorted_keys[-2],"(%1d)"%sorted_values[-2],"\n")
    print("1st Least Line:",sorted_keys[0],"(%1d)"%sorted_values[0],"\n")
    print("2nd Least Line:",sorted_keys[1],"(%1d)"%sorted_values[1],"\n")

if __name__ == '__main__':
    main()
