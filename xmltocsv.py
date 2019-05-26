import csv
import re
import xml.etree.ElementTree as ET


def convertXMLtoCSV():
    mydoc = ET.parse('data.xml')  
    root = mydoc.getroot()
    for elem in root:
        rowarr = [] 
        colarr =[]
        # print(elem.tag)
        if elem.tag == 'COLUMNS':
            col = elem.text
            cvalue = re.split(r'\t',col)
            cvalue.pop(0)
            cvalue.pop(-1)
            colarr.append(cvalue)
            # print(colarr)
            with open('data.csv', 'a') as writeFile:
                writer = csv.writer(writeFile,delimiter=',')
                writer.writerows(colarr)
        if elem.tag == 'DATA':
        #    print(elem.text)
            data = elem.text
            data = data.encode('utf-8')
            value = re.split(r'\t', data)
            value.pop(0)
            value.pop(-1)
            rowarr.append(value)
            # print rowarr
            with open('data.csv', 'a') as writeFile:
                    writer = csv.writer(writeFile,delimiter=',')
                    writer.writerows(rowarr)
convertXMLtoCSV()
