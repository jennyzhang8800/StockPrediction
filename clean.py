import csv
class Solution(object):
    #读csv
    def readCsv(self,csv_name):
        csv_reader = csv.reader(open(csv_name))
        return csv_reader
    
    def cleanData(self,csv_reader):
        out = open(r'E:\stock\data_new.csv', 'w', newline='')
        csv_writer = csv.writer(out, dialect='excel')
        for row in csv_reader:
            data=[]
            #把x_0到x_49进行数据缺失的处理。缺失的数据用前一个补。如果x_0缺失，则用向后找的第一个数据补
            for i in range(3,53):
                if(row[i]=="" ):
                    #x_0缺失
                    if(i==3):
                        for j in row[3:53]:
                            if j!="":
                                row[i]=j
                                break
                    #用前一个补
                    else:
                        row[i]=row[i-1]
            #只保留id,x_0,..x_49,y
            data.append(row[0])
            for j in row[3:53]:
                data.append(j)
            data.append (row[1])
            csv_writer.writerow(data)
    #写csv
    def writeCsv(self,csv_name,data):
        out = open(csv_name, 'w', newline='')
        csv_writer = csv.writer(out, dialect='excel')
        csv_writer.writerow(data)

if __name__ =='__main__':
    s = Solution()
    csv_reader=s.readCsv(r'E:\stock\data.csv')
    s.cleanData(csv_reader)

